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
            self.assertEqual(output, "")  # Check if output is empty

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")  # Check if output is empty

    def test_help_show_command(self):
        """Test the help command for 'show'"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Prints the string representation of a specific instance", output)
            self.assertIn("Usage: show <class name> <id>", output)
            # Add more assertions based on expected help text

    # Add more test methods to cover all commands and features of the console
    # Use the recommended patching technique to intercept STDOUT

if __name__ == '__main__':
    unittest.main()

