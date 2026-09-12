from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    ContextTypes,
    MessageHandler,
    filters
) 
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



async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    text = update.message.text      # text = "Salom"

    await update.message.reply_text(f"Xabaringizni oldim. \nQuyidagi xabarni yozdingiz: \n{text}")


async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    photo = update.message.photo[-1]

    photo_id = photo.file_id

    username = update.effective_user.username

    file = await context.bot.get_file(photo_id)

    filename = f"photos/{username}.jpg"

    await file.download_to_drive(filename)

    await update.message.reply_photo(photo_id)




async def get_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    video = update.message.video

    video_id = video.file_id

    username = update.effective_user.username

    file = await context.bot.get_file(video_id)

    filename = f"videos/{username}.mp4"

    await file.download_to_drive(filename)

    await update.message.reply_video(video_id)




async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    audio = update.message.audio


    audio_id = audio.file_id

    name = audio.file_name

    file = await context.bot.get_file(audio_id)

    filename = f"audios/{name}"

    await file.download_to_drive(filename)

    await update.message.reply_audio(audio_id)




app = Application.builder().token(env.BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("info", get_info))
app.add_handler(CommandHandler("help", get_help))
app.add_handler(CommandHandler("about", about))

app.add_handler(MessageHandler(filters.TEXT, get_text))
app.add_handler(MessageHandler(filters.PHOTO, get_photo))
app.add_handler(MessageHandler(filters.VIDEO, get_video))
app.add_handler(MessageHandler(filters.AUDIO, get_audio))






print("Bot ishga tushdi...")
app.run_polling()   # run_webhook


