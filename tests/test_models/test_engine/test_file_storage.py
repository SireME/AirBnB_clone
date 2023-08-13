#!/usr/bin/python3
"""Test case for the FileStorage module"""
import unittest
import os
import contextlib
import json
import models
import pep8

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_pep8_conformance_file_storage(self):
        """Test PEP8 style conformance"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 issues")

    def setUp(self):
        """Set up the test environment"""

        self.base_model = BaseModel()
        self.amenity = Amenity()
        self.city = City()
        self.place = Place()
        self.review = Review()
        self.state = State()
        self.user = User()
        self.storage = FileStorage()
        self.storage.save()
        if not os.path.exists("file.json"):
            os.mknod("file.json")

    def tearDown(self):
        """Tear down the test environment"""

        del self.base_model
        del self.amenity
        del self.city
        del self.place
        del self.review
        del self.state
        del self.user
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_method(self):
        """Test the all method"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_not_empty(self):
        """Test that the storage is not empty"""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Test the type of the storage"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new_user(self):
        """Test adding a new user"""
        obj = self.storage.all()
        self.user.id = 1234
        self.user.name = "Julien"
        self.storage.new(self.user)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """Test if methods from Storage Engine work"""
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """Test if methods from Storage Engine work"""
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Test the docstrings for each function"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()

