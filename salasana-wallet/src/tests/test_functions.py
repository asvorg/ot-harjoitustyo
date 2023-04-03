import unittest
import pytest
import main
from main import functions


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_password_length(self):
        length = 10
        test_length = functions.generate_password(length)
        if length != len(test_length):
            return False

    def test_generate_password_type(self):
        with self.assertRaises(TypeError):
            functions.generate_password("A")