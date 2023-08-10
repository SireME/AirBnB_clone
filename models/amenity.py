#!/usr/bin/env python3
"""
This module contatins a class that contains amenity info
the class inherits from the BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel
    containinamenity name
    """
    name = ""
