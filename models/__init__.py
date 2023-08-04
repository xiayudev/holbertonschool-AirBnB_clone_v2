#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBstorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
    storage = FileStorage()
    storage.reload()
