from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import env


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    user_id = update.effective_user.id
    is_bot = update.effective_user.is_bot
    language_code = update.effective_user.language_code
    username = update.effective_user.username

    if last_name == None:
        last_name = ""

    if is_bot == True:
        is_bot = "Bot ekansiz"
    else:
        is_bot = "Bot emassiz" 

    if username == None:
        username = "Yo'q"

    reply_text =  f"""
        Assalomu alaykum, {first_name} {last_name}.

        Siz haqizda quyida ma'lumotlar bor menda:
        1. Telegram ID: {user_id}
        2. username: @{username}
        3. Telegramni {language_code} shu tilda ishlatasiz.
        4. {is_bot}.
    """ 
    
    await update.message.reply_text(reply_text)

async def cheksiz_salom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while True:
        reply_text = update.message.reply_text("Salom")
        await reply_text

app = Application.builder().token(env.BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cheksiz_salom", cheksiz_salom))


print("Bot ishga tushdi...")
app.run_polling()   # run_webhook


