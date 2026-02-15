from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config.config import config
from apps.start import start
from apps.

Base.metadata.create_all(bind=engine)

def main() -> None:
    
    
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    
    dispatcher.add_handler(MessageHandler(Filters.text("Shaxsingizni tasdiqlang! 🪪"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tganman!✅"), check_register))
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()