#!/usr/bin/python3
"""
Module that creates
users using inherited BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user inherited from basemodel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
