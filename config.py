#Create a config.py file in the project directory to 
# store your configuration settings, like secret key, 
# database configurations, and other settings.

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database_name.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # other configurations
