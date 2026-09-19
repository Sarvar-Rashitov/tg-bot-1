from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application, 
    ContextTypes, 
    CommandHandler,
    MessageHandler, 
    filters,
    CallbackQueryHandler,
)

from env import BOT_TOKEN

app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    keyboard = [
        [
            InlineKeyboardButton("profile", callback_data="profile"),
            InlineKeyboardButton("settings", callback_data="settings")
        ],

        [
            InlineKeyboardButton("Help center", callback_data="help"),
        ],

        [
            InlineKeyboardButton("About of Company", url="https://ipeschool.uz")
        ],

        [
            InlineKeyboardButton("Telegram chanel", url="https://t.me/ipeschool")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    first_name = update.effective_user.first_name
    text = f"""
Xush kelibsiz, {first_name}.

Bu IPE School telegram boti.

Quyidagi tugmalardan birini tanlang:
"""
    await update.message.reply_text(text, reply_markup=reply_markup)


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    query = update.callback_query

    await query.answer("Profile loading...")

    text = f"""
Profile page.

username: @{update.effective_user.username}
First name: {update.effective_user.first_name}
"""
    await query.message.reply_text(text)




app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(profile, pattern="^profile$"))

print("Bot ishga tushdi...")
app.run_polling()