from telegram.ext import Application, CommandHandler

BOT_TOKEN = "YOUR_BOT_TOKEN"

async def start(update, context):
    await update.message.reply_text("Leech Bot Working Successfully!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()
