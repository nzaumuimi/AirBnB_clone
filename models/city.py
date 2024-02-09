#!/usr/bin/python3
"""Classes that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes to manage state_id and name"""
    state_id = ""
    name = ""
