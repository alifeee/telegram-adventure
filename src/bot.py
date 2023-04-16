import os
from dotenv import load_dotenv
import logging
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


load_dotenv()
try:
    API_KEY = os.environ['TELEGRAM_BOT_ACCESS_TOKEN']
except KeyError:
    raise ValueError(
        "Please set the TELEGRAM_BOT_ACCESS_TOKEN environment variable."
    )

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Use /start to begin your adventure."
    )


def main() -> None:
    application = Application.builder().token(API_KEY).build()

    application.add_handler(CommandHandler("help", help))

    application.run_polling()


if __name__ == "__main__":
    main()
