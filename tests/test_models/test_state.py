#!/usr/bin/python3
"""Module for test state"""
from unittest import TestCase
from models.state import State
from models.base_model import BaseModel
from .test_class import TestClassDocumentation


class TestState(TestCase):
    """Test cases for State"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, State)
        t.documentation()
        t.pep8(['models/state.py', 'tests/test_models/test_state.py'])

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)
