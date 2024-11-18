#!/usr/bin/env python3
"""
This module defines a SQLAlchemy model for a User, mapping to a users table.
The model is used to store and manage user-related data such as email,
hashed password, session ID, and reset token.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    """
    User model for the users table in the database.

    Attributes:
        id (int): Primary key, unique identifier for the user.
        email (str): User's email address, non-nullable.
        hashed_password (str): User's hashed password, non-nullable.
        session_id (str): Session ID for the user's active session, nullable.
        reset_token (str): Token for password reset functionality, nullable.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

if __name__ == "__main__":
    """
    This script ensures that the user.py file is executable.
    It creates the necessary database schema for the User model.
    """
    engine = create_engine('sqlite:///users.db')  # Adjust database URI as needed
    Base.metadata.create_all(engine)
