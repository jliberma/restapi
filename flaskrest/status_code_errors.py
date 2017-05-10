from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
app = Flask(__name__)


def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not found: ' + request.url,
            }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()


if __name__ == '__main__':
    app.run()
