# -*- encoding: utf-8 -*-
# ! python3

from django.test import TestCase


class DummyTestCase(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)
