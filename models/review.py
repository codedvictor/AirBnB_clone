#!/usr/bin/python3
""" Define the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the Reviez class attributes"""
    place_id = ""
    user_id = ""
    text = ""
