from pprint import pprint

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def get_table_content():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://coinmarketcap.com/')
    # Since Height of CoinMarketPlace is 10k+ and data loads on scroll - we are using scrollBy 1000 to complete
    # refreshed data
    javaScript = "window.scrollBy(0, 1000);"
    for i in range(10):
        driver.execute_script(javaScript)

    table = driver.find_element(By.CLASS_NAME, 'bFzXgL')
    table_ihtml = table.get_attribute('innerHTML')
    driver.quit()
    return table_ihtml


def parse_table_content(html_data):
    thead = BeautifulSoup(html_data, features="html.parser")("thead")[0]("th")
    tbody = BeautifulSoup(html_data, features="html.parser")("tbody")[0]("tr")
    response = {
        'head_data': [cell.getText() for cell in thead][2:-2],
        'row_data': [[cell.text for cell in row("td")][2:-2] for row in tbody]
    }
    return response


if __name__ == '__main__':
    data = parse_table_content(get_table_content())
    print(data)
