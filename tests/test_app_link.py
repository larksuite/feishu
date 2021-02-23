# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from tests.conf import TestConfig, app_1_app_id, app_1_app_secret, app_1_cli, app_1_cli_lark, conf, lark_cli


class TestAppLink(unittest.TestCase):

    def test_open_cli(self):
        assert app_1_cli.app_link().open_client() == 'https://applink.feishu.cn/client/op/open'
        assert app_1_cli_lark.app_link().open_client() == 'https://applink.larksuite.com/client/op/open'

    def test_open_mini(self):
        e1 = 'https://applink.feishu.cn/client/mini_program/open?appId=app_id'
        assert app_1_cli.app_link().open_mini_program('app_id') == e1

        e2 = 'https://applink.feishu.cn/client/mini_program/open?appId=app_id&path=pages%252fhome'
        assert app_1_cli.app_link().open_mini_program('app_id', path='pages%2fhome') == e2

        e3 = 'https://applink.feishu.cn/client/mini_program/open?appId=app_id&path=pages%252fhome&min_lk_ver_pc=3.4.0'
        assert app_1_cli.app_link(min_lk_ver_pc='3.4.0').open_mini_program('app_id', path='pages%2fhome') == e3

    def test_open_chat(self):
        e1 = 'https://applink.feishu.cn/client/mini_program/open?openId=id1'
        assert app_1_cli.app_link().open_chat('id1') == e1

        e2 = 'https://applink.feishu.cn/client/mini_program/open?openChatId=id2'
        assert app_1_cli.app_link().open_chat(open_chat_id='id2') == e2
