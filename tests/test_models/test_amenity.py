#!/usr/bin/python3
"""Module for testing the Amenity class"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the implementation of the Amenity class"""
    def test_module_documentation(self):
        """Test module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Test PEP8 conformance for models/amenity.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test PEP8 conformance for tests/test_models/test_amenity.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        files_to_check = ['tests/test_models/test_amenity.py']
        res = pep8style.check_files(files_to_check)
        self.assertEqual(res.total_errors, 0,
                         "Detected code style errors (and warnings) in files: {}".format(files_to_check))

    def test_constructor_documentation(self):
        """Test constructor documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of the class attributes"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()

