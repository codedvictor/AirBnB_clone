#!/usr/bin/python3
""" Define unittest for State class"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Unittests for testing instantiation of Place Class"""

    pl = Place()

    def testPlace_class(self):
        """Tests if an instance of the Place is an instance of
        Place class"""
        self.assertEqual(Place, type(self.pl))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(Place(), storage.all().values())

    def testPlace_inheritance(self):
        """ Test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.pl, BaseModel)

    def testHasAttributes(self):
        """ Test if State has all attributes"""
        self.assertTrue(hasattr(self.pl, 'city_id'))
        self.assertTrue(hasattr(self.pl, 'user_id'))
        self.assertTrue(hasattr(self.pl, 'name'))
        self.assertTrue(hasattr(self.pl, 'description'))
        self.assertTrue(hasattr(self.pl, 'number_rooms'))
        self.assertTrue(hasattr(self.pl, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl, 'max_guest'))
        self.assertTrue(hasattr(self.pl, 'price_by_night'))
        self.assertTrue(hasattr(self.pl, 'latitude'))
        self.assertTrue(hasattr(self.pl, 'longitude'))
        self.assertTrue(hasattr(self.pl, 'amenity_ids'))
        self.assertTrue(hasattr(self.pl, 'id'))
        self.assertTrue(hasattr(self.pl, 'created_at'))
        self.assertTrue(hasattr(self.pl, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.pl.city_id, str)
        self.assertIsInstance(self.pl.user_id, str)
        self.assertIsInstance(self.pl.name, str)
        self.assertIsInstance(self.pl.description, str)
        self.assertIsInstance(self.pl.number_rooms, int)
        self.assertIsInstance(self.pl.number_bathrooms, int)
        self.assertIsInstance(self.pl.max_guest, int)
        self.assertIsInstance(self.pl.price_by_night, int)
        self.assertIsInstance(self.pl.latitude, float)
        self.assertIsInstance(self.pl.longitude, float)
        self.assertIsInstance(self.pl.amenity_ids, list)
        self.assertIsInstance(self.pl.id, str)
        self.assertIsInstance(self.pl.created_at, datetime)
        self.assertIsInstance(self.pl.updated_at, datetime)

    def test_two_places(self):
        """ Tests if 2 places has different ids"""
        pl = Place()
        pl2 = Place()
        self.assertNotEqual(pl.id, pl2.id)


if __name__ == '__main__':
    unittest.main()
