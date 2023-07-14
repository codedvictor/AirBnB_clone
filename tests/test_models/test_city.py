#!/usr/bin/python3
""" Define unittest for City class"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime


class TestCity(unittest.TestCase):
    """ Unittests for testing instantiation of City Class"""

    ct = City()

    def testCity_class(self):
        """Tests if an instance of the City is an instance of
        City class"""
        self.assertEqual(City, type(self.ct))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(City(), storage.all().values())

    def testCity_inheritance(self):
        """ Test if City is a subclass of BaseModel"""
        self.assertIsInstance(self.ct, BaseModel)

    def testHasAttributes(self):
        """ Test if City has all attributes"""
        self.assertTrue(hasattr(self.ct, 'name'))
        self.assertTrue(hasattr(self.ct, 'state_id'))
        self.assertTrue(hasattr(self.ct, 'id'))
        self.assertTrue(hasattr(self.ct, 'created_at'))
        self.assertTrue(hasattr(self.ct, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.ct.name, str)
        self.assertIsInstance(self.ct.state_id, str)
        self.assertIsInstance(self.ct.id, str)
        self.assertIsInstance(self.ct.created_at, datetime)
        self.assertIsInstance(self.ct.updated_at, datetime)

    def test_two_places(self):
        """ Tests if 2 cities has different ids"""
        ct = City()
        ct2 = City()
        self.assertNotEqual(ct.id, ct2.id)


if __name__ == '__main__':
    unittest.main()
