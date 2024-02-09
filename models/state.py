#!/usr/bin/python3
"""Classes that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class attributes to manage name"""
    name = ""
