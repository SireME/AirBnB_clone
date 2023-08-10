#!/usr/bin/env python3
"""
class with state of name inheriting form base class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class to define the state of individual
    """
    name = ""
