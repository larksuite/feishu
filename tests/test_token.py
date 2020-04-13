# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from tests.conf import TestConfig, conf, lark_cli


class TestToken(unittest.TestCase):
    def test_token(self):
        assert lark_cli
        assert lark_cli.app_access_token
        assert lark_cli.tenant_access_token
