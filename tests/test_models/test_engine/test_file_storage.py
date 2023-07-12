#!/usr/bin/python3
""" Module of file storage test """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ Class suite for File Storage Tests """

    model = BaseModel()

    def testInstance(self):
        """ Check fileStorage class instance """
        self.assertIsInstance(storage, FileStorage)

    def testAll(self):
        """ Test all and reload method """
        self.model.name = "BaseModel 1"
        self.model.save()
        m_dict = self.model.to_dict()
        all_objs = storage.all()

        key = "{}.{}".format(m_dict['__class__'], m_dict['id'])
        self.assertEqual(key in all_objs, True)

    def testUpdate(self):
        """ Test all, reload and update method """
        self.model.name = "First Model"
        self.model.save()
        m_dict = self.model.to_dict()
        all_objs = storage.all()

        key = "{}.{}".format(m_dict['__class__'], m_dict['id'])

        self.assertEqual(key in all_objs, True)
        self.assertEqual(m_dict['name'], "First Model")

        create1 = m_dict['created_at']
        update1 = m_dict['updated_at']

        self.model.name = "Second Model"
        self.model.save()
        m_dict = self.model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = m_dict['created_at']
        update2 = m_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(m_dict['name'], "Second Model")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """verify if JSON exists"""
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """test if reload all objects"""
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        all_objs = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(all_objs, FileStorage._FileStorage__objects)
        storage.reload()
        for (k, v) in storage.all().items():
            self.assertEqual(all_objs[k].to_dict(), v.to_dict())

    def test_save_self(self):
        """ Check save with self """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_new(self):
        """ Test if 'new' method is working good """
        dic = self.model.to_dict()
        new_k = "{}.{}".format(dic['__class__'], dic['id'])
        storage.save()
        with open("file.json", 'r') as f:
            jeson = json.load(f)
            keys = jeson[new_k]
            for k in keys:
                self.assertEqual(dic[k], keys[k])


if __name__ == '__main__':
    unittest.main()
