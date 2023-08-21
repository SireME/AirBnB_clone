#!/usr/bin/python3
"""Module for testing the City class
   ensuring functions run accordingly
"""
import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the implementation of the City class"""
    def test_module_documentation(self):
        """Test module documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """Test PEP8 conformance for models/city.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test PEP8 conformance for tests/test_models/test_city.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_constructor_documentation(self):
        """Test constructor documentation"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of the class attributes"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
