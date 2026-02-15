from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config.config import config
from config.database import Base, engine
from config.models import User

from apps.start import start, help, send_idea
from apps.menu import send_menu
from apps.profile import profile
from apps.register import check_register
from apps.conversation import Register, Post


Base.metadata.create_all(bind=engine)

def main() -> None:
    
    
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('tezzbot', send_menu))
    
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tish! 🪪"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tganman!✅"), check_register))
    
    dispatcher.add_handler(MessageHandler(Filters.text("Profilim 👤"), profile))
    dispatcher.add_handler(MessageHandler(Filters.text("Menularga qaytish! ↩️"), send_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("Taklif-Mulohazalar-Yordam💡"), send_idea))
    
    dispatcher.add_handler(Register.register_conversation_handler)
    dispatcher.add_handler(Post.cargo_conv)
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()