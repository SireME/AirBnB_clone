#!/usr/bin/python3
"""
   This Module is to ensure that the User class works
   as expected
"""
import unittest
import json
import pep8
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the implementation of the User class"""
    def test_module_documentation(self):
        """Test module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_user(self):
        """Test PEP8 conformance for models/user.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test PEP8 conformance for tests/test_models/test_user.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_constructor_documentation(self):
        """Test constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of the class attributes"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
