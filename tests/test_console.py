<<<<<<< HEAD
=======
#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import os
import sys
>>>>>>> 62f20a7bdcec8b33dbcfdcc301c32aac5face827
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
from console import HBNBCommand

class TestHBNBCommandUpdate(unittest.TestCase):

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_attr_value_space_notation(self):
        correct = "** value missing **"
        models = [BaseModel, User, State, City, Place, Amenity, Review]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model.__name__}")
                test_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                test_cmd = f"update {model.__name__} {test_id} attr_name"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_valid_string_attr_space_notation(self):
        models = [BaseModel, User, State, City, Place, Amenity, Review]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model.__name__}")
                test_id = output.getvalue().strip()
            test_cmd = f"update {model.__name__} {test_id} attr_name 'attr_value'"
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            test_dict = storage.all()[f"{model.__name__}.{test_id}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    # ... (other test methods)

class TestHBNBCommandCount(unittest.TestCase):

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        models = [BaseModel, User, State, City, Place, Amenity, Review]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model.__name__}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{model.__name__}.count()"))
                self.assertEqual("1", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

