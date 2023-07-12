#!/usr/bin/python3
"""This module recreate a BaseModel
from another one by using a
dictionary representation
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file
    to instances
    """

    __file_path = "file.json"
    __objects = {}

    object_class = {"BaseModel": BaseModel}

    def all(self):
        """return dict object"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets new objects with key id"""
        new_object = "{}.{}".format(type(obj).__name__,
                                    obj.id)
        FileStorage.__objects[new_objects] = obj

    def save(self):
        """serialize __object to JSON file in file path"""
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, 'w',
                  encoding="UTF-8") as dest_file:
            json.dumps(new_dict, dest_file)

    def reload(self):
        """deserializes the JSON file to object if file path exist"""
        try:
            with open(FileStorage.__file_path, 'r',
                      encoding="UTF-8") as dest_file:
                read_objects = json.load(dest_file)

                new_object_class = ["BaseModel"]

                for key, value in read_objects.items():
                    if value.get("__class__") in new_object_class:
                        met = value.get("__class__")
                        self.__objects[key] = eval(str(
                            met))(read_objects[key])
        except Exception:
            pass
