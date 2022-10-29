#!/usr/bin/python3
"""Module for test amenity"""
from unittest import TestCase
from models.amenity import Amenity
from models.base_model import BaseModel
from .test_class import TestClassDocumentation


class TestAmenity(TestCase):
    """Test cases for Amenity"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, Amenity)
        t.documentation()
        t.pep8(['models/amenity.py', 'tests/test_models/test_amenity.py'])

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)
