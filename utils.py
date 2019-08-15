#! /bin/python
# utils setting
#
# @file: utils
# @time: 2019/08/07
# @author: Mori
#

import json
import yaml

import sys
import traceback
import logging

from flask import Response
from typing import Dict


class BaseError(Exception):

    def __init__(self, code, msg):
        super(BaseError, self).__init__()
        self.code = code
        self.msg = msg

def error_handler(err):
    if isinstance(err, BaseError):
        return template_jsonify({}, err.msg, err.code)
    else:
        msg = ''.join(traceback.format_exception(*sys.exc_info()))
        logging.error(msg)
        return template_jsonify({}, msg, 500)


def load_config() -> Dict:
    with open('config.yaml', 'r') as file:
        config = yaml.load(file)
    return config


def template_jsonify(
    data: Dict,
    msg: str = 'OK',
    code: int = 0,
) -> Response:
    http_code = 200
    if code > 200 and code < 600:
        http_code = code
    return Response(
        json.dumps(
            {
                'status': {
                    'code': code,
                    'msg': msg
                },
                'data': data
            }
        ),
        status=http_code,
        mimetype='application/json'
    )
