class Config:
    # General Config
    SECRET_KEY = 'your_secret_key'

    # Database settings
database_user = 'your_db_user'
database_password = 'your_db_password'
database_host = 'your_db_host'
database_name = 'your_db_name'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{{database_user}}:{{database_password}}@{{database_host}}/{{database_name}}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
