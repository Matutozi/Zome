#!/usr/bin/python3
"""Configuration settings for Zome app"""
from os import getenv
from urllib.parse import quote_plus


MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PWD = getenv("MYSQL_PWD")
MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_DB = getenv("MYSQL_DB")
print(MYSQL_USER)
print(MYSQL_PWD)
print(MYSQL_HOST)



class Config:
    """Congirations Class"""
    
    encoded_password = quote_plus(getenv("MYSQL_PWD"))
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{getenv('MYSQL_USER')}:{encoded_password}@{getenv('MYSQL_HOST')}/{getenv('MYSQL_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print(f"Database URI: {Config.SQLALCHEMY_DATABASE_URI}")
