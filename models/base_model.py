#!/usr/bin/python3

"""
Module that defines parent class for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Class that defines all common attributes/methods
    for others classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize attributes"""

        fmat = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for (k, v) in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(kwargs[k], fmat)
                if k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string for printing a class instance
        """
        cls_name = "[" + self.__class__.__name__ + "]"
        dic = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return (cls_name + " (" + self.id + ") " + str(dic))

    def save(self):
        """Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionnary containing all keys/values of
        __dict__ of the instance"""

        new_dict = {}
        fmat = "%Y-%m-%dT%H:%M:%S.%f"
        for (k, v) in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                new_dict[k] = v.strftime(fmat)
            else:
                if not v:
                    pass
                else:
                    new_dict[k] = v

        new_dict['__class__'] = self.__class__.__name__

        return new_dict
