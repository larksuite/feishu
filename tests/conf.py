# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import io
import json
import logging
import os
import unittest

import attr

from feishu import OpenLark
from feishu.dt_help import make_datatype, to_json_decorator


@to_json_decorator
@attr.s
class TestConfigBot(object):
    app_id = attr.ib(type=str, default='')
    app_secret = attr.ib(type=str, default='')
    oauth_redirect_uri = attr.ib(type=str, default='')


@to_json_decorator
@attr.s
class TestConfigALLBot(object):
    open_lark = attr.ib(type=TestConfigBot, default=None)


# test config
# some read from github secret
# some read from local json file
@to_json_decorator
@attr.s
class TestConfig(object):
    bot = attr.ib(type=TestConfigALLBot, default=None)  # 机器人配置

    lark_app_id = attr.ib(type=str, default='')
    lark_app_secret = attr.ib(type=str, default='')

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


def _get_conf():
    with open('./tests/conf.json', 'r') as f:
        v = json.load(f)
        conf = make_datatype(TestConfig, v)  # type: TestConfig

    logging.info('[test] local json conf is %s', conf)

    conf.lark_app_id = os.getenv('APP_ID_1')
    conf.lark_app_secret = os.getenv('APP_SECRET_1')
    conf.bot.open_lark.app_secret = os.getenv(conf.bot.open_lark.app_secret)

    return conf


conf = _get_conf()
lark_cli = OpenLark(conf.lark_app_id, conf.lark_app_secret, oauth_redirect_uri='oauth_redirect_uri')
