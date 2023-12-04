#!/usr/bin/python3
"""Configuration settings for Zome app"""
from os import getenv

MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PWD = getenv("MYSQL_PWD")
MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_DB = getenv("MYSQL_DB")


class Config:
    """Congirations Class"""
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(
        MYSQL_USER,
        MYSQL_PWD,
        MYSQL_HOST,
        MYSQL_DB
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
