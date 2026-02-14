from telegram.ext import Updater
from config.config import config
def main() -> None:
    
    
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher