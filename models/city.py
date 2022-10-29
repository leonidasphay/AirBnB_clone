#!/usr/bin/python3
"""Module"""
from .base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseModel"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
