#!/usr/bin/python3
""" Define unittest for amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Unittests for testing instantiation of Amenity Class"""

    am = Amenity()

    def testAmenity_class(self):
        """Tests if an instance of Amenity is an instance of
        Amenity class"""
        self.assertEqual(Amenity, type(self.am))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(Amenity(), storage.all().values())

    def testAmenity_inheritance(self):
        """ Test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.am, BaseModel)

    def testHasAttributes(self):
        """ Test if Amenity has all attributes"""
        self.assertTrue(hasattr(self.am, 'name'))
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime)
        self.assertIsInstance(self.am.updated_at, datetime)

    def test_two_amenities(self):
        """ Tests if 2 amenities has different ids"""
        am = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am.id, am2.id)


if __name__ == '__main__':
    unittest.main()
