import json
import time
from pprint import pprint

import requests
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
    for i in range(11):
        driver.execute_script(javaScript)

    table = driver.find_element(By.CLASS_NAME, 'bFzXgL')
    table_ihtml = table.get_attribute('innerHTML')
    driver.quit()
    return table_ihtml


def parse_table_content(html_data):
    # thead = ['name','price','1h','24h','7d','market_cap','volume24h','supply']
    tbody = BeautifulSoup(html_data, features="html.parser")("tbody")[0]("tr")
    row_data = []
    for row in tbody:
        td_data = row('td')[2:-2]
        try:
            temp_data = {
                'id': int(td_data[0].findAll('div', class_='hDTQEj')[0].getText()),
                'name': td_data[0].findAll('p', class_="lhJnKD")[0].getText(),
                'code': td_data[0].findAll('p', class_="emEbFH")[0].getText(),
                'img': td_data[0]('img')[0]['src'],
                'price': td_data[1].getText(),
                '1h': td_data[2].getText(),
                '24h': td_data[3].getText(),
                '7d': td_data[4].getText(),
                'market_cap': td_data[5].findAll('span', class_="iosgXe")[0].getText(),
                'volume24h': td_data[6].findAll('p', class_="fVSMmK")[0].getText() + " | "+td_data[6].findAll('p', class_="hueJdC")[0].getText(),
                'supply': td_data[7].getText(),
            }
            row_data.append(temp_data)
        except Exception as e:
            pass

    return row_data


def update_coin_data(insert_flag):
    _url = 'http://localhost:5000/coin/insert' if insert_flag else 'http://localhost:5000/coin/update'
    payload = {
        "data": parse_table_content(get_table_content())
    }
    x = requests.post(_url, json=payload)
    return json.loads(x.text)


if __name__ == '__main__':
    insert_flag = True  # this flag can be set in env so that we dont insert everytime when we restart scrapper
    while True:
        resp = update_coin_data(insert_flag)
        if insert_flag:
            if 'err_detail' in resp and 'duplicate key value violates unique constraint' in resp['err_detail']:
                resp = update_coin_data(False)
            insert_flag = False
        print(resp)
        time.sleep(5)  # Schedule Cron Job on Server to scrap instead of while loop
