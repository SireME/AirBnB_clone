#!/usr/bin/env python3
"""
This module contatins a class that contains xity info
the class inherits from the BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
