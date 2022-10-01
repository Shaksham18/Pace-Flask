from pyApp.endpoints import *


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Content-type, Authorization, Origin, X-Requested-With'
    response.headers['Allow'] = '*'
    return response


if __name__ == '__main__':
    app.run()
