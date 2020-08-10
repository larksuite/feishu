# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest


class TestVersion(unittest.TestCase):
    def test_version(self):
        from open_lark import __version__
        assert '0.0.1' == __version__
