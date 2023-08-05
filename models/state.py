#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        city = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""
