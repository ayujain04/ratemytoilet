import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://your_username:your_password@localhost:5432/your_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
