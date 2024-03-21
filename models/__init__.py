#!/usr/bin/python3
""" this module instantiates an object of the  class FileStorage """
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""a unique FileStorage/DBStorage instance for all the models
"""
storage.reload()
