"""Test the code functions"""

import unittest
from unittest.mock import patch
import io

class TestFunctions(unittest.TestCase):
    """Test the program functions"""

    def setUp(self):
        self.test_user = "test_user"
        self.test_password = "test_password"
        self.test_service = "test_service"

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

    @patch('builtins.input', side_effect=["new_user", "testpassword"])
    def test_create_user(self, mock_inputs):
        functions.create_user()
        self.assertEqual("new_user", functions.persistent.users_dict.keys()[0])
        self.assertEqual(64, len(functions.persistent.users_dict.values()[0]))

        @patch('builtins.input', side_effect=["test_user", "testpassword"])
        def test_existing_user(self, mock_inputs):
            functions.persistent.users_dict = {"test_user": "fakehash"}
            with unittest.patch('builtins.print') as mock_print:
                functions.create_user()
                mock_print.assert_called_with("Already in use")
            self.assertEqual({"test_user": "fakehash"},
                             functions.persistent.users_dict)

    def test_add_password(self):
        add_password_user_input = self.test_user + '\n'
        add_password_masterpassword_input = self.test_password + '\n'
        add_password_service_input = self.test_service + '\n'
        add_password_password_input = "test_password" + '\n'
        expected_output = "Added password for user test_user for service test_service\n"

        with unittest.mock.patch('builtins.input', side_effect=[add_password_user_input,
                                                                add_password_masterpassword_input,
                                                                add_password_service_input,
                                                                add_password_password_input]):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                functions.add_password()
                self.assertEqual(fake_stdout.getvalue(), expected_output)

    def tearDown(self):
        if (self.test_user, self.test_service) in persistent.user_stored_passwords:
            del persistent.user_stored_passwords[(
                self.test_user, self.test_service)]

    def test_padding(self):
        password_to_pad = "password"
        padded_password = functions.pad(password_to_pad)
        self.assertEqual(
            padded_password,
            "password\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

        password_to_pad = "thisisaverylongpassword"
        padded_password = functions.pad(password_to_pad)
        self.assertEqual(padded_password, password_to_pad)

        password_to_pad = ""
        padded_password = functions.pad(password_to_pad)
        self.assertEqual(padded_password, "\x00" * 32)
