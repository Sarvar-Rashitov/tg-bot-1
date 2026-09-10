from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import env


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text(f"Salom, {update.effective_user.first_name}")


async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
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



async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    
    help_text = f"""
Botimizga Xush kelibsiz!

Bu quyidagi comandalar bor:
1. /start - botni ishga tushurish
2. /info  - siz haqizda ma'lumot
3. /about - biz haqimizda
4. /help  - yordam markazi

Qo'shimcha yordam uchun @Sarvar_Rashitov
"""
    await update.message.reply_text(help_text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    await update.message.reply_text("Biz IPE School o'quvchilarimiz")

app = Application.builder().token(env.BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("info", get_info))
app.add_handler(CommandHandler("help", get_help))
app.add_handler(CommandHandler("about", about))


print("Bot ishga tushdi...")
app.run_polling()   # run_webhook


