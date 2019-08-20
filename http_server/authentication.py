import json
import time
import base64
import hmac
from http_server.db import SearrchORM

# 解密
def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return 'token错误'
    ts_str = token_list[0]
    if float(ts_str) < time.time():
    # token expired
        return 'token已过期，请更新'

        # return 0
    known_sha1_tsstr = token_list[1]
    calc_sha1_tsstr = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1').hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
    # token certification failed
        return'token不匹配'
    # token certification success
    else:
        return 'ok'



