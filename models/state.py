#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import os

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (os.HBNB_TYPE_STORAGE == "db"):
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            "return the list of City objects"
            dict_all_cities = self.all(City)
            list_cities = []
            for city in dict_all_cities.values():
                if city.id == self.state_id:
                    list_cities.append(city)
            return list_cities
            