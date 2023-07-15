#!/usr/bin/python3
"""
Module that creates
users using inherited BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user inherited from basemodel
    Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
