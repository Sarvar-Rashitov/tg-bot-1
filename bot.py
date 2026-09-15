from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler
)
from env import BOT_TOKEN, chanel_username, hr_chat_id

import os 
from dotenv import load_dotenv

load_dotenv()
app = Application.builder().token(os.getenv("BOT_TOKEN")).build()

FULL_NAME, PHONE, PHOTO = range(3)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print(update.effective_user.id)

    context.user_data["username"] = update.effective_user.username
    await update.message.reply_text(f"Xush kelibsiz, {update.effective_user.first_name} \nFISH kiriting: ")

    return FULL_NAME


async def get_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["full_name"] = update.message.text
    await update.message.reply_text("FISH gizni qabul qildim, Endi telifon raqamingizni jo'nating: ")

    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["phone"] = update.message.text
    await update.message.reply_text("Telifon raqamingizni qabul qildim, Endi rasmingizni jo'nating: ")
    
    return PHOTO

async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["photo"] = update.message.photo[-1].file_id
    await update.message.reply_text("Rasmingizni qabul qildim. Ma'lumotni jo'natish uchun /cancel bosing")
    
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_photo(
        chat_id=chanel_username,
        photo=context.user_data["photo"],
        caption=f"""
Yangi qatnashuvchi @{context.user_data["username"]}

FISH: {context.user_data["full_name"]}.
tell: {context.user_data["phone"]}
"""
    )


    await context.bot.send_photo(
            chat_id=hr_chat_id,
            photo=context.user_data["photo"],
            caption=f"""
    Yangi qatnashuvchi @{context.user_data["username"]}
    
FISH: {context.user_data["full_name"]}.
tell: {context.user_data["phone"]}
"""
        )


converstation = ConversationHandler(
    entry_points=[
        CommandHandler("start", start),
    ],
    states={
        FULL_NAME: [
            MessageHandler(filters.TEXT, get_full_name)
        ],

        PHONE: [
            MessageHandler(filters.TEXT, get_phone)
        ],

        PHOTO: [
            MessageHandler(filters.PHOTO, get_photo)
        ],
    },
    fallbacks=[]
)


app.add_handler(converstation)
app.add_handler(CommandHandler("cancel", cancel))





app.run_polling()
