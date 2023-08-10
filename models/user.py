#!/usr/bin/env python3
"""
This module contatins a class that contains user info
the class inherits from the BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    with class user attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
