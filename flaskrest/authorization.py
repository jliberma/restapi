from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
from functools import wraps


app = Flask(__name__)


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    resp.status_code = 401
    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/secrets')
@requires_auth
def api_hello():
    return "Shhhh this is top secret spy stuff\n"


if __name__ == '__main__':
    app.run()
