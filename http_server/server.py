import json
import time
import base64
import hmac
from flask import Flask, request
from http_server.db import SearrchORM
from utils import template_jsonify
from zerorpc import Client
from utils import BaseError, error_handler
from .authentication import certify_token

app = Flask(__name__)


@app.route('/index', methods=['POST'])
def index():

    mqtt_client = Client()
    mqtt_client.connect('tcp://127.0.0.1:2048')
    if not request.args:
        return "未传token"
    else:
        token = request.args.get('token').encode()
        str_token=token.decode('utf-8')
        action = request.get_json()
        print(action)

    sql_data = json.dumps(SearrchORM.select_user(str_token))
    print(sql_data)
    # 鉴权
    certify_token(key=sql_data, token=token)

    # 调用下发指令
    print(
        mqtt_client.dispatch_action(
            'lua/test/data/456',
            action
        )
    )
    # response
    return template_jsonify({})


@app.route("/test_project", methods=['GET','POST'])
def test_project():
    if request.method == 'POST':
        msg = request.data.decode()
        print(msg)
        SearrchORM.data_save(msg)
        return msg

    elif request.method == 'GET':
        sql_data = json.dumps(SearrchORM.select_msg())
        print(sql_data)
        return sql_data


@app.route("/token")
def verify(expire=36000):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    # 加密  哈希
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    data = json.dumps({
        'username': username,
        'password':password
    })

    sha1_tshexstr = hmac.new(data.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    print(type(b64_token))
    print(type(b64_token.decode('utf-8')))
    SearrchORM.user_save(username, password, b64_token)

    return b64_token.decode("utf-8")


@app.errorhandler(Exception)
def _error_handler(e):
    return error_handler(e)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )

