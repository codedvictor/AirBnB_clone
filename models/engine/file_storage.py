#!/usr/bin/python3
"""This module recreate a BaseModel
from another one by using a
dictionary representation
"""
import json
import os


class FileStorage:
    """This class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file
    to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict object"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets new objects with key id"""
        new_object = "{}.{}".format(type(obj).__name__,
                                    obj.id)
        FileStorage.__objects[new_object] = obj

    def save(self):
        """serialize __object to JSON file in file path"""
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w',
                  encoding="UTF-8") as dest_file:
            json.dump(new_dict, dest_file)

    def reload(self):
        """deserializes the JSON file to object if file path exist"""
        from models.base_model import BaseModel
        from models.user import User

        dic = {
            'BaseModel': BaseModel,
            'User': User
        }

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r',
                      encoding="UTF-8") as dest_file:
                read_objects = json.load(dest_file)

                for k, v in read_objects.items():
                    self.new(dic[v['__class__']](**v))
