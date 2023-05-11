"""Test the code functions"""

import unittest
import pytest
from unittest.mock import patch
from pymongo import MongoClient, errors
import io
import main.utils.functions as functions
import main.utils.persistent as persistent


class TestFunctions(unittest.TestCase):
    """Test the program functions"""

    def setUp(self):
        self.test_user = "test_user"
        self.test_password = "test_password"
        self.test_service = "test_service"

    @patch('builtins.input', return_value='10')
    def test_generate_password(self, mock_input):
        """Test generate_password function"""
        password = functions.generate_password()
        self.assertIsInstance(password, str)
        self.assertEqual(len(password), 10)

    @patch('builtins.input', return_value='invalid')
    def test_generate_password_invalid_input(self, mock_input):
        """Test generate_password function with invalid input"""
        with self.assertRaises(TypeError):
            functions.generate_password()

    def test_pad(self):
        """Test the pad function"""
        password = 'short_password'
        padded_password = functions.pad(password)
        expected_padded_password = password + ('\x00' * (32 - len(password)))
        self.assertEqual(padded_password, expected_padded_password)

        password = 'a' * 32
        padded_password = functions.pad(password)
        self.assertEqual(padded_password, password)

        with pytest.raises(ValueError, match="Password must be less than 32 characters"):
            password = 'long_password' * 10
            padded_password = functions.pad(password)

    def test_unpad(self):
        """Test the unpad function"""
        padded_password = 'padded_password\x00\x00\x00'
        unpadded_password = functions.unpad(padded_password)
        expected_unpadded_password = 'padded_password'
        self.assertEqual(unpadded_password, expected_unpadded_password)


