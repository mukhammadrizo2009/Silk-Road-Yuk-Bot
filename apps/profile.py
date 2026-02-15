from telegram import (Update , ReplyKeyboardMarkup , KeyboardButton)
from telegram.ext import CallbackContext
from sqlalchemy.orm import Session
from config.dependencies import get_db 
from config.models import User

def profile(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    telegram_id = update.message.from_user.id
    
    db: Session = next(get_db())
    
    try:
        user = db.query(User).filter(User.telegram_id == telegram_id).first()
        
        if user:
            name = user.name if user.name else "Kiritilmagan"
            phone_number = user.phone_number if user.phone_number else "Kiritilmagan"
            
            profile_text = (
                "👤 <b>Sizning profilingiz:</b>\n\n"
                f"📝 Ism: {name}\n"
                f"☎️ Telefon: {phone_number}\n"
            )
            update.message.reply_text(profile_text, parse_mode='HTML')
           
            update.message.reply_text(
            "Ma'lumotlaringiz bilan tanishing!",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("Menularga qaytish! ↩️")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))
    
        else:
            update.message.reply_text(
                "❌ Sizning ma'lumotlaringiz topilmadi."
            )
    finally:
        db.close()