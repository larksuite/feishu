# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from tests.conf import TestConfig, conf, lark_cli


class TestOAuth(unittest.TestCase):
    def test_oauth(self):
        oauth_url = lark_cli.gen_oauth_url('state')
        assert oauth_url
        assert oauth_url == 'https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri=' \
                            'oauth_redirect_uri&app_id={}&state=state'.format(conf.lark_app_id)
