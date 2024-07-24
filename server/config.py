import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:6789@localhost/ecommerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
