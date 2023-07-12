#!/bin/usr/python3
"""
Init for engine model module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
