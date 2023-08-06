#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skip("showing class skipping")
class test_basemodel(unittest.TestCase):
    """ """

    @unittest.skip("demonstrating skipping")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @unittest.skip("demonstrating skipping")
    def setUp(self):
        """ """
        pass

    @unittest.skip("demonstrating skipping")
    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    @unittest.skip("demonstrating skipping")
    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skip("demonstrating skipping")
    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skip("demonstrating skipping")
    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skip("demonstrating skipping")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skip("demonstrating skipping")
    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skip("demonstrating skipping")
    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skip("demonstrating skipping")
    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("demonstrating skipping")
    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    @unittest.skip("demonstrating skipping")
    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skip("demonstrating skipping")
    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skip("demonstrating skipping")
    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
