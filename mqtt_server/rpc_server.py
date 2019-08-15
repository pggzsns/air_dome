from .mqtt_server import MQTTServer
from zerorpc import Server


if __name__ == '__main__':

    server = Server(MQTTServer)
    server.bind('tcp://0.0.0.0:2048')
    server.run()