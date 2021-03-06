from flask import Flask, url_for
from flask import request
from flask import json
app = Flask(__name__)


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data + "\n"
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json) + "\n"
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!\n"
    else:
        return "415 Unsupported Media Type\n"


if __name__ == '__main__':
        app.run()
