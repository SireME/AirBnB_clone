#!/usr/bin/python3
"""Module for testing the Amenity class"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test implementation of the Amenity class"""
    def test_module_documentation(self):
        """Ensure there is documentation for the module"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py adheres to PEP8 guidelines."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Encountered code style errors and warnings.")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Discovered code style errors and warnings.")

    def test_constructor_documentation(self):
        """Ensure there is documentation for the constructor"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of attributes within the class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)


if __name__ == '__main__':
    unittest.main()

