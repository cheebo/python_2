from unittest import TestCase
from py_01 import middleChar


class Test(TestCase):
    def test_middle_char_even(self):
        self.assertEqual(middleChar("test"), "es")

    def test_middle_char_odd(self):
        self.assertEqual(middleChar("testing"), "t")
