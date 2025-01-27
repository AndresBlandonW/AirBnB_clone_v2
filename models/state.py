#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id"""
            from models.engine.file_storage import FileStorage
            from models.city import City
            files = FileStorage.all(City)
            city_list = []
            for key, value in files.items():
                if 'City' in key and self.id == value.state_id:
                    city_list.append(value)
            return city_list
