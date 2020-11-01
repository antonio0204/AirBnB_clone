#!/usr/bin/python3
"""
Define Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """State class that enherits from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
