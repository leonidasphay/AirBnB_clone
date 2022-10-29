#!/usr/bin/python3
"""Module for test city"""
from unittest import TestCase
from models.city import City
from models.base_model import BaseModel
from .test_class import TestClassDocumentation


class TestCity(TestCase):
    """Test cases for State"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, City)
        t.documentation()
        t.pep8(['models/city.py', 'tests/test_models/test_city.py'])

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)
