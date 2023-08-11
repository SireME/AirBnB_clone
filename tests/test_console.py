#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing the console"""

    def create_instance(self):
        """Create an instance of HBNBCommand"""
        return HBNBCommand()

    def test_quit_command(self):
        """Test the quit command"""
        console_instance = self.create_instance()
        self.assertTrue(console_instance.onecmd("quit"))

    def test_eof_command(self):
        """Test the EOF command"""
        console_instance = self.create_instance()
        self.assertTrue(console_instance.onecmd("EOF"))

