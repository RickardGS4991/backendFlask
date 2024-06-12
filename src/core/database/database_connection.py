import os

class Config:
    #Es una mala práctica agregar información para el acceso a la BD, pero esto lo hago simplemente para este proyecto.
    #Nunca debes de hacerlo tú
    db_user = os.environ.get('DATABASE_USER', 'root')
    db_password = os.environ.get('DATABASE_PASSWORD', 'rootpassword')
    db_host = os.environ.get('DATABASE_HOST', 'db')
    db_name = os.environ.get('DATABASE_NAME', 'flights')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False