#!/usr/bin/env python3
"""User Module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

"""A SQLAlchemy model named User with id, email, hashed_password,
session_id and reset_token attributes"""


class User(Base):
    """

    Database table named users
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
