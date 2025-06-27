import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Railway dagi .env ga yoziladi

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    webapp_url = "https://luckylife-signal.vercel.app"  # <-- BU YERGA O'Z VERCEL LINKINGIZNI YOZING!

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="🚀 Open", web_app=WebAppInfo(url=webapp_url))]
    ])

    await update.message.reply_text(
        "📡 Signal paneliga kirish uchun 'Open' tugmasini bosing:",
        reply_markup=keyboard
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
