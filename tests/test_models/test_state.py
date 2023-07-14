#!/usr/bin/python3
""" Define unittest for State class"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """ Unittests for testing instantiation of State Class"""

    st = State()

    def testState_class(self):
        """Tests if an instance of the State is an instance of
        State class"""
        self.assertEqual(State, type(self.st))

    def test_instance_store_in_objects(self):
        """ Tests if a new instance is store in the file"""
        self.assertIn(State(), storage.all().values())

    def testState_inheritance(self):
        """ Test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.st, BaseModel)

    def testHasAttributes(self):
        """ Test if State has all attributes"""
        self.assertTrue(hasattr(self.st, 'name'))
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def testTypes(self):
        """ Test if the attributes types are correct"""
        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime)
        self.assertIsInstance(self.st.updated_at, datetime)

    def test_two_places(self):
        """ Tests if 2 places has different ids"""
        st = State()
        st2 = State()
        self.assertNotEqual(st.id, st2.id)


if __name__ == '__main__':
    unittest.main()
