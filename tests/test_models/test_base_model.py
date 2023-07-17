#!/usr/bin/python3

"""Module for the test_base_model class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from io import StringIO


class BaseModelsTests(unittest.TestCase):
    """ Base model test class """

    model = BaseModel()

    def testAttributes(self):
        """ Test attributes values """
        self.model.name = "House"
        self.model.my_number = 12
        model_json = self.model.to_dict()

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

        self.assertEqual(self.model.id, model_json['id'])
        self.assertEqual(self.model.name, model_json['name'])
        self.assertEqual(self.model.my_number, model_json['my_number'])
        self.assertEqual('BaseModel', model_json['__class__'])

    def test_str(self):
        """ Test the str magic method """
        res = "[BaseModel] ({}) {}".format(self.model.id,
                                           str(self.model.__dict__))

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(self.model)
            self.assertEqual(std_out.getvalue(), res + '\n')

    def test_kwargs(self):
        """ Test the creation of an instance of BaseModel using kwargs """
        dic_m = self.model.to_dict()
        model_new = BaseModel(**dic_m)
        self.assertEqual(model_new.id, self.model.id)
        self.assertEqual(model_new.created_at, self.model.created_at)
        self.assertEqual(model_new.updated_at, self.model.updated_at)

    def testSave(self):
        """ Test the save method with created_at and updated_at """
        self.model.name = "House"
        self.model.save()

        dict_a = self.model.to_dict()

        self.model.name = "Building"
        self.model.save()

        dict_b = self.model.to_dict()

        self.assertEqual(dict_a['created_at'], dict_b['created_at'])
        self.assertNotEqual(dict_a['updated_at'], dict_b['updated_at'])

    def testSave2(self):
        """ Test the save method """
        model = BaseModel()
        update = model.updated_at
        model.save()

        self.assertNotEqual(update, model.updated_at)


if __name__ == '__main__':
    unittest.main()
