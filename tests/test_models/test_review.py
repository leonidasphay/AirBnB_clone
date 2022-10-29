#!/usr/bin/python3
"""Module for test Review"""
from unittest import TestCase
from models.review import Review
from models.base_model import BaseModel
from .test_class import TestClassDocumentation


class TestReview(TestCase):
    """Test cases for State"""

    def test_code_review(self):
        """Test documentation and pep8"""
        t = TestClassDocumentation(self, Review)
        t.documentation()
        t.pep8(['models/review.py', 'tests/test_models/test_review.py'])

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.text, str)
            self.assertIsInstance(Review.user_id, str)
