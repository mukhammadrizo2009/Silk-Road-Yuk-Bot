from datetime import datetime, timedelta

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ConversationHandler, CallbackContext
)
from config.config import post, config, REGIONS, CITY_TOPICS

def start_cargo(update: Update, context: CallbackContext):
    context.user_data.clear()

    keyboard = []
    row = []

    for region in REGIONS:
        row.append(InlineKeyboardButton(region, callback_data=region))
        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "📍 Yuk qayerdan jo'natiladi?",
        reply_markup=reply_markup
    )
    
    return post.FROM

def get_from(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    context.user_data["from"] = query.data

    keyboard = []
    row = []

    for region in REGIONS:
        row.append(InlineKeyboardButton(region, callback_data=region))
        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(f"📍 Qayerdan: {query.data}")
    query.message.reply_text(
        "📍 Yuk qayerga olib boriladi?",
        reply_markup=reply_markup
    )

    return post.TO



def get_to(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()


    context.user_data["to"] = query.data

    query.edit_message_text(f"📍 Qayerga: {query.data}")


    query.message.reply_text("📦 Yuk turi (mebel, oziq-ovqat va h.k)?")

    return post.TYPE



def get_type(update: Update, context: CallbackContext):
    context.user_data["type"] = update.message.text
    update.message.reply_text("⚖️ Og'irligi (kg yoki tonna)?")
    return post.WEIGHT


def get_weight(update: Update, context: CallbackContext):
    context.user_data["weight"] = update.message.text
    update.message.reply_text("🚛 Transport (misol: Labo)?")
    return post.VOLUME


def manual_date(update: Update, context: CallbackContext):
    
    text = update.message.text.strip()

    try:
        
        from datetime import datetime
        date_obj = datetime.strptime(text, "%d.%m.%Y")
        context.user_data["date"] = date_obj.strftime("%d.%m.%Y")

        update.message.reply_text(
            f"📅 Jo'natish sanasi: {context.user_data['date']}\n💰 Taklif narxi?"
        )

        return post.PRICE

    except ValueError:
        
        update.message.reply_text(
            "❌ Sana noto‘g‘ri formatda. Iltimos quyidagi formatda yozing: dd.mm.yyyy\nMasalan: 25.02.2026"
        )
        return post.DATE


def get_volume(update: Update, context: CallbackContext):
    context.user_data["volume"] = update.message.text

    keyboard = [
        [InlineKeyboardButton("📅 Bugun", callback_data="today")],
        [InlineKeyboardButton("📅 Ertaga", callback_data="tomorrow")],
        [InlineKeyboardButton("📆 Sana tanlash", callback_data="custom")]
    ]

    update.message.reply_text(
        "📅 Qachon jo'natiladi?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return post.DATE


def get_date(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "today":
        date = datetime.now().strftime("%d.%m.%Y")

    elif query.data == "tomorrow":
        date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

    else:
        query.edit_message_text("📆 Sana yozing (masalan: 25.02.2026)")
        return post.DATE

    context.user_data["date"] = date
    query.edit_message_text(f"📅 Jo'natish sanasi: {date}")
    query.message.reply_text("💰 Taklif narxi?")
    return post.PRICE


def get_price(update: Update, context: CallbackContext):
    context.user_data["price"] = update.message.text
    update.message.reply_text("📞 Telefon raqamingiz? (misol: +998 90 123 4567)")
    return post.PHONE


def get_phone(update: Update, context: CallbackContext):
    context.user_data["phone"] = update.message.text

    keyboard = [
        [InlineKeyboardButton("⏭ O‘tkazib yuborish", callback_data="skip_comment")]
    ]

    update.message.reply_text(
        "📝 Izoh (agar bo‘lsa yozing, bo‘lmasa tugmani bosing)",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return post.COMMENT

def skip_comment(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    context.user_data["comment"] = "Yo‘q"

    query.edit_message_text("📝 Izoh: Yo‘q")
    return finish(update, context)



def finish(update: Update, context: CallbackContext):

    message = update.effective_message
    query = update.callback_query

    if query:
        query.answer()
        comment_text = context.user_data.get("comment", "Yo‘q")
    else:
        comment_text = message.text

    context.user_data["comment"] = comment_text
    data = context.user_data

    text = f"""
📦 *Yangi yuk e’loni*

📍 {data['from']} ➡️ {data['to']}
📦 Yuk turi: {data['type']}
⚖️ Og‘irlik: {data['weight']}
🚛 Transport: {data['volume']}
📅 Sana: {data['date']}
💰 Narx: {data['price']}
📞 Telefon: {data['phone']}
📝 Izoh: {data['comment']}
"""

    keyboard = [
        ["📤 Guruhga yuborish"],
        ["❌ Bekor qilish"]
    ]

    message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    )

    return post.CONFIRM




def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("❌ Bekor qilindi.")
    return ConversationHandler.END




def send_to_group(update: Update, context: CallbackContext):

    data = context.user_data

    text = f"""
📦 *Yangi yuk e’loni*

📍 {data['from']} ➡️ {data['to']}
📦 Yuk turi: {data['type']}
⚖️ Og‘irlik: {data['weight']}
🚛 Transport: {data['volume']}
📅 Sana: {data['date']}
💰 Narx: {data['price']}
📞 Telefon: {data['phone']}
📝 Izoh: {data['comment']}
"""

    topics = set()

    from_city = data.get("from", "").upper()
    to_city = data.get("to", "").upper()

    if from_city in CITY_TOPICS:
        topics.add(CITY_TOPICS[from_city])

    if to_city in CITY_TOPICS:
        topics.add(CITY_TOPICS[to_city])

    for topic_id in topics:
        context.bot.send_message(
            chat_id=config.SUPERGROUP_ID,
            text=text,
            parse_mode="Markdown",
            message_thread_id=topic_id
        )

    update.message.reply_text(
        "✅ E'lon muvaffaqiyatli yuborildi!",
        reply_markup=ReplyKeyboardRemove()
    )

    context.user_data.clear()

    return ConversationHandler.END
