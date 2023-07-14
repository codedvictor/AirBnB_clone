#!/usr/bin/python3
""" Define unittest for Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """ Unittests for testing instantiation of Review Class"""

    rv = Review()

    def testReview_class(self):
        """Tests if an instance of the Review is an instance of
        Review class"""
        self.assertEqual(Review, type(self.rv))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(Review(), storage.all().values())

    def testReview_inheritance(self):
        """ Test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.rv, BaseModel)

    def testHasAttributes(self):
        """ Test if Review has all attributes"""
        self.assertTrue(hasattr(self.rv, 'place_id'))
        self.assertTrue(hasattr(self.rv, 'user_id'))
        self.assertTrue(hasattr(self.rv, 'text'))
        self.assertTrue(hasattr(self.rv, 'id'))
        self.assertTrue(hasattr(self.rv, 'created_at'))
        self.assertTrue(hasattr(self.rv, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.rv.place_id, str)
        self.assertIsInstance(self.rv.user_id, str)
        self.assertIsInstance(self.rv.text, str)
        self.assertIsInstance(self.rv.id, str)
        self.assertIsInstance(self.rv.created_at, datetime)
        self.assertIsInstance(self.rv.updated_at, datetime)

    def test_two_reviews(self):
        """ Tests if 2 reviews has different ids"""
        rv = Review()
        rv2 = Review()
        self.assertNotEqual(rv.id, rv2.id)


if __name__ == '__main__':
    unittest.main()
