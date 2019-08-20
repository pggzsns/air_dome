# from flask import Flask, request
# import json
# import time
# import base64
# import hmac
# from user_server.db import UserORM
#
# app = Flask(__name__)
#
# @app.route("/token")
# def verify(expire=36000):
#     ts_str = str(time.time() + expire)
#     ts_byte = ts_str.encode("utf-8")
#     # 加密  哈希
#     username = request.form.get('username')
#     password = request.form.get('password')
#     print(username)
#     print(password)
#     data = json.dumps({
#         'username': username,
#         'password':password
#     })
#
#     sha1_tshexstr = hmac.new(data.encode("utf-8"), ts_byte, 'sha1').hexdigest()
#     token = ts_str + ':' + sha1_tshexstr
#     b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
#     print(type(b64_token))
#     print(type(b64_token.decode('utf-8')))
#     UserORM.user_save(username, password, b64_token)
#
#     return b64_token.decode("utf-8")
#
#
# # 解密
# def certify_token(token):
#     token_str = base64.urlsafe_b64decode(token).decode('utf-8')
#     token_list = token_str.split(':')
#     print(token_list)
#     if len(token_list) != 2:
#         print('token_list!=2, 返回0')
#         return 'token错误'
#     ts_str = token_list[0]
#     print('token时间:'+str(ts_str))
#     print('当前时间:'+ str(time.time()))
#     if float(ts_str) < time.time():
#     # token expired
#         return 'token已过期，请更新'
#
#
#
# if __name__ == '__main__':
#     app.run(
#         debug=True,
#         port=8080,
#         host='0.0.0.0'
#     )