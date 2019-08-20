# import pymysql
# import json
# from utils import load_config
# from typing import Tuple, Dict
# from pymysql.connections import Connection as MysqlConnection
#
#
# class UserORM(object):
#     # 数据库配置
#     _mysql_client = None
#
#     @classmethod
#     def sql_client(cls) -> MysqlConnection:
#         if not cls._mysql_client:
#             MYSQL_CONFIG = load_config()['mysql']
#             cls._mysql_client = MysqlConnection(
#                 host=MYSQL_CONFIG['host'],
#                 user=MYSQL_CONFIG['username'],
#                 passwd=MYSQL_CONFIG['password'],
#                 database=MYSQL_CONFIG['db'],
#                 port=MYSQL_CONFIG['port'],
#                 cursorclass=pymysql.cursors.DictCursor
#             )
#
#         return cls._mysql_client
#
#
#     @classmethod
#     def user_save(cls, username: str, password:str, token:str) -> bool:
#         with cls.sql_client().cursor() as cursor:
#             try:
#                 data = {
#                     'username': username,
#                     'password': password,
#                     'token': token,
#                 }
#                 cursor.execute(
#                     # 'INSERT INTO user (`msg`) VALUES (%(msg)s)', data)
#                     'INSERT INTO user (`username`, `password`, `token`) VALUES (%(username)s, %(password)s, %(token)s)', data)
#
#             except Exception as e:
#                 print(e)
#                 return False
#         cls.sql_client().commit()
#         return True
#
#
#     # @classmethod
#     # def select_msg(cls) -> bool:
#     #     with cls.sql_client().cursor() as cursor:
#     #         cursor.execute(
#     #             'SELECT * FROM ari202')
#     #         result = cursor.fetchall()
#     #     return result