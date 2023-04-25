"""Test the code functions"""

import unittest
from main import functions#,persistent


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_password_length(self):
        """Test if generate_password returns proper length"""
        length = 10
        test_length = functions.generate_password(length)
        if length != len(test_length):
            return False
        return True

    def test_generate_password_type(self):
        """Test if the generate_password function returns proper type"""
        with self.assertRaises(TypeError):
            functions.generate_password("A")
