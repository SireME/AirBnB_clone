#!/usr/bin/python3
"""Module for testing the Place class"""
import unittest
import json
import pep8
import datetime

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test implementation of the Place class"""
    def test_module_documentation(self):
        """Ensure there is documentation for the module"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_place(self):
        """Test that models/place.py adheres to PEP8 guidelines."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Encountered code style errors and warnings.")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Discovered code style errors and warnings.")

    def test_constructor_documentation(self):
        """Ensure there is documentation for the constructor"""
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of attributes within the class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()

