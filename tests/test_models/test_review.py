#!/usr/bin/python3
"""
  This Modul is to ensure that the Review class
  works accordingly
"""
import unittest
import json
import pep8
import datetime

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the implementation of the Review class"""
    def test_module_documentation(self):
        """Test module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Test PEP8 conformance for models/review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test PEP8 conformance for tests/test_models/test_review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_constructor_documentation(self):
        """Test constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of the class attributes"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
