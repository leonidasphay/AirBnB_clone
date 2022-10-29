#!/usr/bin/python3
"""Module"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
