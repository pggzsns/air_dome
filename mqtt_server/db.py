import pymysql

from utils import load_config
from typing import Tuple, Dict
from pymysql.connections import Connection as MysqlConnection


class MsgORM(object):
    # 数据库配置
    _mysql_client = None

    @classmethod
    def sql_client(cls) -> MysqlConnection:
        if not cls._mysql_client:
            MYSQL_CONFIG = load_config()['mysql']
            cls._mysql_client = MysqlConnection(
                host=MYSQL_CONFIG['host'],
                user=MYSQL_CONFIG['username'],
                passwd=MYSQL_CONFIG['password'],
                database=MYSQL_CONFIG['db'],
                port=MYSQL_CONFIG['port'],
                cursorclass=pymysql.cursors.DictCursor
            )

        return cls._mysql_client

    @classmethod
    def save(cls, msg: str) -> bool:
        with cls.sql_client().cursor() as cursor:
            try:
                data = {
                    'msg': msg,
                }
                cursor.execute(
                    'INSERT INTO msg (`msg`) VALUES (%(msg)s)', data)
            except Exception as e:
                print(e)
                return False
        cls.sql_client().commit()
        return True