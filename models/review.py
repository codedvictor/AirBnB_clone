#!/usr/bin/python3
""" Define the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the Review class attributes
    Public class attributes:
    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
