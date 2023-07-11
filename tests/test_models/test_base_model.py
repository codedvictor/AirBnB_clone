#!/usr/bin/python3

"""Module for the test_base_model class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


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


if __name__ == '__main__':
    unittest.main()
