#!/usr/bin/python3
"""Module for testing the State class"""
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test implementation of the State class"""
    def test_module_documentation(self):
        """Ensure there is documentation for the module"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """Test that models/state.py adheres to PEP8 guidelines."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Encountered code style errors and warnings.")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Discovered code style errors and warnings.")

    def test_constructor_documentation(self):
        """Ensure there is documentation for the constructor"""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of attributes within the class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()

