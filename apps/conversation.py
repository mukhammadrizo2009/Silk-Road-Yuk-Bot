from telegram.ext import MessageHandler, ConversationHandler, Filters, CommandHandler

from config.config import register_states, post

from apps.register import get_name, set_name, set_phone, save_user
from apps.cargo import start_cargo, get_from, get_type, get_to, get_weight, get_volume, get_date, get_price, get_phone, finish, cancel, skip_comment, manual_date, send_to_group

class Register():
    register_conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("📝 Ro'yhatdan o'tishni boshlash..!") , get_name)],
    states={
        register_states.NAME: [MessageHandler(Filters.text, set_name)],
        register_states.PHONE_NUMBER: [MessageHandler(Filters.contact, set_phone)],
        
        register_states.CONFIRM: [
            MessageHandler(Filters.regex("^Tasdiqlash! ✅$"), save_user),
            MessageHandler(Filters.regex("^Tahrirlash! ♻️$"), get_name),
        ]
    },
    fallbacks = []
    )
    
from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler, CallbackQueryHandler

class Post:
    cargo_conv = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex("^📦 E'lon berish$"), start_cargo)
        ],
        states={post.FROM: [CallbackQueryHandler(get_from)],
        post.TO: [CallbackQueryHandler(get_to)],
        post.TYPE: [MessageHandler(Filters.text & ~Filters.command, get_type)],
        post.WEIGHT: [MessageHandler(Filters.text & ~Filters.command, get_weight)],
        post.VOLUME: [MessageHandler(Filters.text & ~Filters.command, get_volume)],
        post.DATE: [CallbackQueryHandler(get_date),MessageHandler(Filters.text & ~Filters.command, manual_date)],
        post.PRICE: [MessageHandler(Filters.text & ~Filters.command, get_price)],
        post.PHONE: [MessageHandler(Filters.text & ~Filters.command, get_phone)],
        post.COMMENT: [CallbackQueryHandler(skip_comment, pattern="^skip_comment$"),MessageHandler(Filters.text & ~Filters.command, finish)],
        post.CONFIRM: [MessageHandler(Filters.regex("📤 Guruhga yuborish"), send_to_group),MessageHandler(Filters.regex("❌ Bekor qilish"), cancel)],
        },
        fallbacks=[],
        allow_reentry=True 
        )
