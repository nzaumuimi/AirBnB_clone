#!/usr/bin/python3
"""Module that inherits class Review from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for Review attributes"""

    place_id = ""
    user_id = ""
    text = ""
