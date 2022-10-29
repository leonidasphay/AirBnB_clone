#!/usr/bin/python3
"""Module for test user"""
from unittest import TestCase
from models.user import User
from models.base_model import BaseModel
from .test_class import TestClassDocumentation


class TestUser(TestCase):
    """Test cases for User"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, User)
        t.documentation()
        t.pep8(['models/user.py', 'tests/test_models/test_user.py'])

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)
