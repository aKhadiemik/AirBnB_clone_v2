#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if models.storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """
    Represents Place on db

    Attributes:
    __tablename__ (str): name places table.
    city_id (sqlalchemy String): city id.
    user_id (sqlalchemy String): user id.
    name (sqlalchemy String): name.
    description (sqlalchemy String): description.
    number_rooms (sqlalchemy Integer): number of rooms.
    number_bathrooms (sqlalchemy Integer): number of bathrooms.
    max_guest (sqlalchemy Integer): max number of guests.
    price_by_night (sqlalchemy Integer): price by night.
    latitude (sqlalchemy Float): latitude.
    longitude (sqlalchemy Float): longitude.
    reviews (sqlalchemy relationship): Place-Review relationship.
    amenities (sqlalchemy relationship): Place-Amenity relationship.
    amenity_ids (list): id list of all linked amenities.
    """
    if models.storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """Gets list of linked Review instances"""
            from models.review import Review
            review_list = []
            reviews = models.storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Gets list of all linked Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            if type(value) == Amenity:
                self.amenity_ids.appedn(value.id)
