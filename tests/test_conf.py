# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import io
import json
import logging
import unittest
import attr

from open_lark.dt_help import make_datatype, to_json_decorator


# test config
# some read from github secret
# some read from local json file
@to_json_decorator
@attr.s
class TestConfig(object):
    email = attr.ib(type=str, default='')
    open_chat_id = attr.ib(type=str, default='')
    open_id = attr.ib(type=str, default='')
    test_department_id = attr.ib(type=str, default='')
    test_employee_id = attr.ib(type=str, default='')
    user_id = attr.ib(type=str, default='')
    open_message_id = attr.ib(type=str, default='')
    message_id = attr.ib(type=str, default='')
    test_definition_code = attr.ib(type=str, default='')
    image_key = attr.ib(type=str, default='')


__conf = {}


def get_conf():
    global __conf
    with open('./conf.json', 'r') as f:
        v = json.load(f)
        conf = make_datatype(TestConfig, v)

    logging.info('[test] local json conf is %s', conf)
