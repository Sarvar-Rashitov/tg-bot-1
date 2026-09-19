from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler
)
from env import BOT_TOKEN

app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    keyboard = [
        [
        InlineKeyboardButton("tugma nomi", callback_data = "salom",)
        ,
        InlineKeyboardButton("tugma nomi", callback_data = "help")
        ],
        [
            InlineKeyboardButton("OBUNA", callback_data="obuna")
        ],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(f"""
Xush kelibsiz, {update.effective_user.first_name}""",

reply_markup=markup 

)

async def check_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    query = update.callback_query
    print(query)


    

    if query.data == "salom":
        await query.answer("Salom")
    elif query.data == "help":
        await query.answer("Yordam markazi!")

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_button))

app.run_polling()
