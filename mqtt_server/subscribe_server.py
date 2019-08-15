from .mqtt_server import MQTTServer


if __name__ == '__main__':
    MQTTServer.subscribe()
    MQTTServer.client().loop_forever()
