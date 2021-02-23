# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from tests.conf import TestConfig, app_1_app_id, app_1_app_secret, app_1_cli, conf, lark_cli


class TestConf(unittest.TestCase):

    def test_conf_v2(self):
        assert app_1_app_id
        assert app_1_app_secret
        assert app_1_cli

    # def test_conf(self):
    #     assert conf
    #     assert conf.lark_app_id
    #     assert conf.lark_app_secret
