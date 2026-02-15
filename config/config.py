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
    SUPERGROUP_ID = os.getenv("GROUP_ID")


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
    CONFIRM = 9
    
    
REGIONS = [
    "Toshkent", "Andijon", "Namangan", "Fargona",
    "Samarqand", "Buxoro", "Navoiy", "Qashqadaryo",
    "Surxondaryo", "Xorazm", "Jizzax", "Qaroqalpoqiston"
]


CITY_TOPICS = {
    "TOSHKENT": int(os.getenv("TOSHKENT")),
    "NAMANGAN": int(os.getenv("NAMANGAN")),
    "SAMARQAND": int(os.getenv("SAMARQAND")),
    "FARGONA": int(os.getenv("FARGONA")),
    "ANDIJON": int(os.getenv("ANDIJON")),
    "BUXORO": int(os.getenv("BUHORO")),
    "SURXONDARYO": int(os.getenv("SURHONDARYO")),
    "QAROQALPOQISTON": int(os.getenv("QAROQALPOQISTON")),
    "NAVOIY": int(os.getenv("NAVOIY")),
    "JIZZAX": int(os.getenv("JIZZAX")),
    "QASHQADARYO": int(os.getenv("QASHQADARYO")),
    "XORAZM": int(os.getenv("XORAZM")),
}


config = Config()
register_states = RegisterStates()
post = Post()