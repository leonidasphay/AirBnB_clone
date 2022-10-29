#!/usr/bin/python3
"""Module"""
from .base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
