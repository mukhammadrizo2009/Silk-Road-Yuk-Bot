import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

class RegisterStates():
    NAME = 0
    PHONE_NUMBER = 1
    CONFIRM = 2
    
class Post():
    FROM = 0
    TO = 1
    TYPE = 2
    WEIGHT = 3
    VOLUME = 4
    DATE = 5
    PRICE = 6
    PHONE = 7
    COMMENT = 8
    
config = Config()
register_states = RegisterStates()
post = Post()