#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            
            f.clear()
            self.console.onecmd("show BaseModel " + obj_id)
            self.assertIn(obj_id, f.getvalue())

if __name__ == '__main__':
    unittest.main()

