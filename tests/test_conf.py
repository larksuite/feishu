# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from tests.conf import TestConfig, conf, lark_cli


class TestConf(unittest.TestCase):
    def test_conf(self):
        assert conf
        assert conf.lark_app_id
        assert conf.lark_app_secret
