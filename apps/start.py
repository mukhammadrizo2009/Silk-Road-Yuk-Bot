from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from config.config import config

#def start(update: Update, context: CallbackContext):
#    bot = context.bot
#    user = update.effective_user
    
#    bot.send_message(
#        chat_id = user.id,
#        text = "✋Assalomu Alaykum!\n\n"
#            "Guruhda e'lon berish uchun, bir martalik ro'yhatdan o'ting!🧾",
#            parse_mode = "markdown",
#            reply_markup = ReplyKeyboardMarkup(
#                keyboard=[
#                    [KeyboardButton("Shaxsingizni tasdiqlang! 🪪"), KeyboardButton("Ro'yhatdan o'tganman!✅")]
#                ],
#                resize_keyboard=True,
#                one_time_keyboard=True
#    ))
    
def start(update: Update, context: CallbackContext):
    bot = context.bot
    
    
    bot.send_message(
    chat_id=config.SUPERGROUP_ID,
    text="Test xabar",
    parse_mode="Markdown",
    message_thread_id=None  # topic_id mavjud emas bo‘lsa asosiy chatga
    )
    print(update.message.message_thread_id)
