from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config.config import config
from config.database import Base, engine

from apps.start import start, debug
from apps.register import check_register
from apps.conversation import Register, Post

Base.metadata.create_all(bind=engine)

def main() -> None:
    
    
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('debug', debug))
    
    dispatcher.add_handler(MessageHandler(Filters.text("Shaxsingizni tasdiqlang! 🪪"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tganman!✅"), check_register))
    
    dispatcher.add_handler(Register.register_conversation_handler)
    dispatcher.add_handler(Post.cargo_conv)
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()