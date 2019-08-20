import pymysql
import json
import requests
from utils import load_config

from typing import Dict
from paho.mqtt.client import Client as MQTTClient
from pymysql.connections import Connection as MysqlConnection
from .db import MsgORM


class MQTTServer(object):
    # 独立运行

    # _mysql_client = None

    # @classmethod
    # def sql_client(cls) -> MysqlConnection:
    #     if not cls._mysql_client:
    #         MYSQL_CONFIG = load_config()['mysql']
    #         cls._mysql_client = MysqlConnection(
    #             host=MYSQL_CONFIG['host'],
    #             user=MYSQL_CONFIG['username'],
    #             passwd=MYSQL_CONFIG['password'],
    #             database=MYSQL_CONFIG['db'],
    #             port=MYSQL_CONFIG['port'],
    #             cursorclass=pymysql.cursors.DictCursor
    #         )

    #     return cls._mysql_client

    # @classmethod
    # def _client_on_connect(cls):
    #     pass
    #
    # @classmethod
    # def _client_on_message(cls):
    #     pass
    #
    # @classmethod
    # def _client_on_publish(cls):
    #     pass
    #
    # @classmethod
    # def _client_on_disconnect(cls):
    #     pass

    # @classmethod
    # def client(cls) -> MQTTClient:
    #     if cls._client is None:
    #         cls._client = MQTTClient()
    #         cls._client.on_connect = cls._client_on_connect
    #         cls._client.on_message = cls._client_on_message
    #         cls._client.on_publish = cls._client_on_publish
    #         cls._client.on_disconnect = cls._client_on_disconnect
    #         MQTT_CONFIG = load_config()['mqtt']
    #         client.username_pw_set(MQTT_CONFIG['username'], MQTT_CONFIG['password'])
    #         client.connect(MQTT_CONFIG['broker'], MQTT_CONFIG['port'], 60)
    #     return cls._client


    # @classmethod
    # def _client_on_message(cls, client, userdata, message):
    #     requests.post('http://192.168.199.139/test_project', data={'payload': message})

    _client = None

    @classmethod
    def client(cls) -> MQTTClient:
        if not cls._client:
            cls._client = MQTTClient()
            MQTT_CONFIG = load_config()['mqtt']
            cls._client.username_pw_set(MQTT_CONFIG['username'], MQTT_CONFIG['password'])
            cls._client.connect(MQTT_CONFIG['broker'], MQTT_CONFIG['port'], 60)
        return cls._client


    # 向终端下发命令
    @classmethod
    def dispatch_action(cls, topic: str, payload: Dict):
        print(topic, payload)
        cls.client().publish(
            topic=topic,
            payload=json.dumps(payload)
        )

    # 接收消息
    @classmethod
    def _client_on_message(cls, client, userdata, message):
        msg = message.payload.decode('utf8')
        print(msg)
        # MsgORM.save(msg)
        print("MSG")
        requests.post('http://192.168.199.139:8080/test_project', data=msg)
        print("POST")


    @classmethod
    def subscribe(cls):
        cls.client().on_message = cls._client_on_message
        cls.client().subscribe('lua/test/data/123')

