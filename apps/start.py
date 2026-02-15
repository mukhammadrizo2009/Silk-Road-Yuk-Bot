from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.utils.helpers import escape_markdown


def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
 
    text = (
    "✋Assalomu Alaykum!\n "
    f"{escape_markdown('@silkroad_loads11', version=1)} \n"
    "Guruhda e'lon berishni boshlash uchun ro'yhatdan o'ting. 😊"
)

    bot.send_message(
    chat_id=user.id,
    text=text,
    parse_mode="Markdown",
    reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Ro'yhatdan o'tish! 🪪"), KeyboardButton("Ro'yhatdan o'tganman!✅")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
)


def help(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user 
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Admin bilan bog'lanish", url="https://t.me/karimov_22222")]
    ])

    bot.send_message(
        chat_id=user.id,
        text="Assalomu alaykum-😊\nSizda bo'layotgan muammo bo'yicha adminga murojaat qiling!",
        reply_markup=keyboard
    )

    
def send_idea(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    text = (
        "🧾Taklif va Mulohazalaringizni bu yerga yozib qoldirishingiz mumkin!😇\n\n"
        f"Username: {escape_markdown('@karimov_22222', version=1)}"
    )

    bot.send_message(
        chat_id=user.id,
        text=text,
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("Menularga qaytish! ↩️")]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
