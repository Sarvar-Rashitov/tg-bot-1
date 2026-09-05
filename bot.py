from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application
import env


app = Application.builder().token(env.BOT_TOKEN).build()

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    return update.message.reply_text(f"Salom {update.effective_user.first_name}")


app.add_handler(CommandHandler("get_lst", start))
app.run_polling()


