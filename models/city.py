#!/usr/bin/python3
""" Define the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Define the City class attribute
    Public class attributes:
    state_id: string - empty string
    name: string - empty string
    """
    state_id = ""
    name = ""
