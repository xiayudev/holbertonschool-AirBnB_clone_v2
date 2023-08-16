#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.state import State


class DBStorage:
    """This class manages storage of hbnb models in the
    database with sqlalchemy
    """
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        h = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{h}/{db}",
                                      pool_pre_ping=True)

    def all(self, cls=None):
        dic = {}
        if cls is not None:
            di = self.__session.query(cls).all()
            for row in di:
                dic[f"{row.__class__.__name__}.{row.id}"] = row
        return dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.query(obj.__class__
                                 ).filter_by(id=obj.id
                                             ).delete(
                                                      synchronize_session=False
                                                      )

    def reload(self):
        """Loads storage dictionary from a database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

        Base.metadata.create_all(self.__engine)

    def close(self):
        """Method on the private session attribute"""
        self.__session.remove()
