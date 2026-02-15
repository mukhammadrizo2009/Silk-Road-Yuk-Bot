from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ConversationHandler, CallbackContext
)
from config.config import post

# 🔵 Yuk joylashni boshlash
def start_cargo(update: Update, context: CallbackContext):
    context.user_data.clear()
    update.message.reply_text("📍 Yuk qayerdan jo'natiladi?", reply_markup=ReplyKeyboardRemove())
    return post.FROM


def get_from(update: Update, context: CallbackContext):
    context.user_data["from"] = update.message.text
    update.message.reply_text("📍 Yuk qayerga olib boriladi?")
    return post.TO


def get_to(update: Update, context: CallbackContext):
    context.user_data["to"] = update.message.text
    update.message.reply_text("📦 Yuk turi (mebel, oziq-ovqat va h.k)?")
    return post.TYPE


def get_type(update: Update, context: CallbackContext):
    context.user_data["type"] = update.message.text
    update.message.reply_text("⚖️ Og'irligi (kg yoki tonna)?")
    return post.WEIGHT


def get_weight(update: Update, context: CallbackContext):
    context.user_data["weight"] = update.message.text
    update.message.reply_text("📐 Hajmi (masalan: 4-tonna)?")
    return post.VOLUME


def get_volume(update: Update, context: CallbackContext):
    context.user_data["volume"] = update.message.text
    update.message.reply_text("📅 Qachon jo'natiladi?")
    return post.DATE


def get_date(update: Update, context: CallbackContext):
    context.user_data["date"] = update.message.text
    update.message.reply_text("💰 Taklif narxi?")
    return post.PRICE


def get_price(update: Update, context: CallbackContext):
    context.user_data["price"] = update.message.text
    update.message.reply_text("📞 Telefon raqamingiz?")
    return post.PHONE


def get_phone(update: Update, context: CallbackContext):
    context.user_data["phone"] = update.message.text
    update.message.reply_text("""📝 Izoh (bo'lmasa "yo'q" deb yozing)""")
    return post.COMMENT


# 🟢 Yakunlash
def finish(update: Update, context: CallbackContext):
    context.user_data["comment"] = update.message.text
    data = context.user_data

    text = f"""
📦 *Yangi yuk e’loni*

📍 {data['from']} ➡️ {data['to']}
📦 Yuk turi: {data['type']}
⚖️ Og‘irlik: {data['weight']}
📐 Hajm: {data['volume']}
📅 Sana: {data['date']}
💰 Narx: {data['price']}
📞 Telefon: {data['phone']}
📝 Izoh: {data['comment']}
"""

    update.message.reply_text(text, parse_mode="Markdown")
    context.user_data.clear()

    keyboard = [["📦 Yuk joylash"], ["🚛 Mashina joylash"]]
    update.message.reply_text(
        "✅ E'lon qabul qilindi!",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("❌ Bekor qilindi.")
    return ConversationHandler.END
