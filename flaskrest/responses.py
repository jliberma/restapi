from flask import Flask, url_for
from flask import Response
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def api_hello():
    data = {
            'hello': 'world',
            'number': 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application.json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp
