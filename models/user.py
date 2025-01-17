#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """
    This class defines a user by various attributes

    Attributes:
    __tablename__ (str): table users on db.
    email: (sqlalchemy String): email address.
    password (sqlalchemy String): password.
    first_name (sqlalchemy String): first name.
    last_name (sqlalchemy String): last name.
    places (sqlalchemy relationship): User-Place relationship.
    reviews (sqlalchemy relationship): User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
