"""Test the code functions"""

import unittest
from unittest.mock import patch
import main.utils.functions as functions
import main.utils.encryption_helpers as eh


class TestFunctions(unittest.TestCase):
    """Test the program functions"""

    def setUp(self):
        """"Tests setup"""
        self.test_user = "test_user"
        self.test_password = "test_password"
        self.test_service = "test_service"

    def test_generate_password_valid_length(self):
        """Test for generating a password with a valid length"""
        with unittest.mock.patch('builtins.input', return_value='8'):
            with unittest.mock.patch('builtins.print') as mock_print:
                functions.generate_password()
                mock_print.assert_called_once()

    def test_generate_password_invalid_length(self):
        """Test for generating a password with an invalid length"""
        with unittest.mock.patch('builtins.input', return_value='abc'):
            with unittest.mock.patch('builtins.print') as mock_print:
                functions.generate_password()
                mock_print.assert_called_with("Length must be an integer")

    def test_generate_password_negative_length(self):
        """Test for generating a password with a negative length"""
        with unittest.mock.patch('builtins.input', return_value='-5'):
            with unittest.mock.patch('builtins.print') as mock_print:
                functions.generate_password()
                mock_print.assert_called_with("Length must be an integer")

    def test_generate_password_zero_length(self):
        """Test for generating a password with a length of zero"""
        with unittest.mock.patch('builtins.input', return_value='0'):
            with unittest.mock.patch('builtins.print') as mock_print:
                functions.generate_password()
                mock_print.assert_called_once()


    def test_valid_input(self):
        """Test the valid input function, so it accepts the valid inputs"""
        valid_inputs = ["c", "cp", "q", "gr", "ap", "l", "d"]
        for input_value in valid_inputs:
            result = functions.validate_input(input_value)
            self.assertTrue(result)

    def test_invalid_input(self):
        """Test invalid inputs"""
        invalid_inputs = ["a", "abc", "123", "", "x", "test"]
        for input_value in invalid_inputs:
            result = functions.validate_input(input_value)
            self.assertFalse(result)

    def test_edge_validate_cases(self):
        """Test empty input"""
        result = functions.validate_input(None)
        self.assertFalse(result)

        result = functions.validate_input(123)
        self.assertFalse(result)

    def test_pad_key(self):
        """"Test the key padding function"""
        key = "mykey"
        expected_padded_key = b"mykey\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c"
        self.assertEqual(eh.pad_key(key), expected_padded_key)

    def test_unpad_key(self):
        """Test the key unpadding function"""
        padded_key = b"mykey\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c"
        expected_key = b"mykey"
        self.assertEqual(eh.unpad_key(padded_key), expected_key)

    def test_pad_string(self):
        """Test the string padding function"""
        password = "password"
        expected_padded_string = "password\x07\x07\x07\x07\x07\x07\x07"
        self.assertEqual(eh.pad_string(password), expected_padded_string)

    def test_encryption_and_decryption(self):
        """"Test encryption and decryption"""
        password = "password"
        key = "mykey"
        encrypted_password = eh.encryption(password, key)
        decrypted_password = eh.decryption(encrypted_password, key)
        self.assertEqual(decrypted_password, password)

    def test_create_user(self, mock_input):
        """"Test user creation"""
        mock_input.side_effect = ['username', 'password']

        with patch('your_module.persistent.initialize_database_users'), \
                patch('your_module.hl.sha256') as mock_sha256, \
                patch('your_module.collection.insert_one') as mock_insert:
            mock_sha256.return_value.hexdigest.return_value = 'hashed_password'
            functions.create_user()

        mock_sha256.assert_called_once_with('password'.encode('utf-8'))
        mock_insert.assert_called_once_with(
            {'username': 'username', 'password': 'hashed_password'})
        self.assertEqual(mock_input.call_count, 2)
