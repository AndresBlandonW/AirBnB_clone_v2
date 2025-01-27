#!/usr/bin/python3
""" Unitttest for HBNBCommand class """
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models import storage
import os


class TestHBNBCommandClass(TestCase):
    """ Tests HBNBCommand class """

    def test_do_create(self):
        """ Test create method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NoClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        HBNBCommand().onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "1\n")

        HBNBCommand().onecmd("create State name=\"Nevada\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "2\n")
