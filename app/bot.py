from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from .instagram import fetch_posts
from .config import BOT_TOKEN, CHANNEL


async def fetch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /fetch mountain")
        return

    keyword = context.args[0]

    try:
        posts = fetch_posts(keyword)

        if not posts:
            await update.message.reply_text("No posts found.")
            return

        for shortcode in posts:
            url = f"https://www.instagram.com/p/{shortcode}/"
            await context.bot.send_message(chat_id=CHANNEL, text=url)

        await update.message.reply_text("✅ Posted successfully")

    except Exception as e:
        await update.message.reply_text(f"❌ Error:\n{e}")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("fetch", fetch))

    print("🤖 Bot started (polling)")
    app.run_polling()


if __name__ == "__main__":
    main()
