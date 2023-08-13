#!/usr/bin/python3
"""Module for testing the State class"""
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the implementation of the State class"""
    def test_module_documentation(self):
        """Test module documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """Test PEP8 conformance for models/state.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test PEP8 conformance for tests/test_models/test_state.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Detected code style errors (and warnings).")

    def test_constructor_documentation(self):
        """Test constructor documentation"""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_attributes(self):
        """Validate the types of the class attributes"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()

