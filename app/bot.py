from telegram.ext import ApplicationBuilder, CommandHandler
from .instagram import fetch_posts
from .limiter import allow
from .config import BOT_TOKEN, CHANNEL, POSTS_PER_HOUR

async def fetch(update, context):
    if not context.args:
        await update.message.reply_text("Usage: /fetch mountain")
        return

    keyword = context.args[0]

    try:
        posts = fetch_posts(keyword, POSTS_PER_HOUR)
    except Exception as e:
        await update.message.reply_text(f"❌ {e}")
        return

    sent = 0
    for link in posts:
        if not allow(POSTS_PER_HOUR):
            await update.message.reply_text("⏳ Hourly limit reached")
            break

        await context.bot.send_message(chat_id=CHANNEL, text=link)
        sent += 1

    await update.message.reply_text(f"✅ Posted {sent} posts")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("fetch", fetch))
    app.run_polling()

if __name__ == "__main__":
    main()
