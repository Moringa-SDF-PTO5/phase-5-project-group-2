import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://group2_electronics_project_user:wYWHOsnDi3EgTzVU0hVb2c7Zt4Fej1wC@dpg-cqch7lmehbks738g4k80-a.frankfurt-postgres.render.com/group2_electronics_project')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
