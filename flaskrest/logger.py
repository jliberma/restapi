from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response


app = Flask(__name__)


import logging
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
#app.run(debug=True)


@app.route('/hello', methods = ['GET'])
def api_hello():
    app.logger.info('informing you that im processing a request')
    app.logger.warning('warning you that im processing a request')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"


if __name__ == '__main__':
    app.run()
