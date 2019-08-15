import json
from flask import Flask, request
from utils import template_jsonify
from zerorpc import Client
from utils import BaseError, error_handler


app = Flask(__name__)


@app.route('/index', methods=['POST'])
def index():
    mqtt_client = Client()
    mqtt_client.connect('tcp://127.0.0.1:2048')
    action = request.get_json()

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
    mqtt_client = Client()
    mqtt_client.connect('tcp://127.0.0.1:2048')
    action = request.get_json()
    print(
        mqtt_client.subscribe()
    )
    # data = json.loads(request.data.get('data'))

    print(str(request.get_data()))
    # return '%s' % (request.get_data() or 'null')
    return '%s' % (action or 'null')
    # return template_jsonify({})

@app.errorhandler(Exception)
def _error_handler(e):
    return error_handler(e)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )