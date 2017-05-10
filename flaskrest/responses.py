from flask import Flask, url_for
from flask import request
from flask import json
from flask import jsonify
from flask import Response
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def api_hello():
    data = {
            'hello': 'world',
            'number': 3
    }
    js = json.dumps(data)

    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

if __name__ == '__main__':
    app.run()
