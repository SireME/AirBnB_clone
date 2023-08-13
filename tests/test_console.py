#!/usr/bin/python3
"""Test for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
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

    def test_show_command(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output
            with patch('sys.stdout', new=StringIO()) as f_show:
                self.console.onecmd("show BaseModel " + instance_id)
                output_show = f_show.getvalue().strip()
                self.assertIn(instance_id, output_show)

    # Add more test methods for other commands and features

if __name__ == '__main__':
    unittest.main()

