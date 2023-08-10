#!/usr/bin/env python3
"""
This module contatins a class that contains review info
the class inherits from the BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    and stores review info
    """
    place_id = ""
    user_id = ""
    text = ""
