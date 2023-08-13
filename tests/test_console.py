#!/usr/bin/python3
"""Test for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing the console"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test environment"""
        pass  # You can add any necessary cleanup here

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create_command(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check if output is not empty

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    # Add test methods for show, destroy, all, and update commands
    # Make sure to test all possible cases mentioned in the requirements

if __name__ == '__main__':
    unittest.main()

