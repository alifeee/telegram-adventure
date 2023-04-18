import os
from dotenv import load_dotenv
import logging
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ConversationHandler,
    filters,
)
from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from database import Database


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


# adventure step returns function
def adventure_step(
        node_id: str,
        ends: list,
        description: str,
        responses: list
):
    buttons = [
        [
            KeyboardButton(response)
        ] for response in responses
    ]

    async def adventure(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.effective_message.reply_text(
            description,
            reply_markup=ReplyKeyboardMarkup(
                buttons, one_time_keyboard=True, resize_keyboard=True, is_persistent=True),
        )
        if node_id in ends:
            await update.effective_message.reply_text(
                "You have reached the end of the adventure. Use /start to begin again.",
                reply_markup=ReplyKeyboardRemove(),
            )
            return ConversationHandler.END
        return node_id

    return adventure


def main() -> None:
    application = Application.builder().token(API_KEY).build()

    application.add_handler(CommandHandler("help", help))

    db = Database("adventure.db")
    node_ids = db.get_all_node_ids()
    descriptions = {
        node_id: db.get_node(node_id)["description"]
        for node_id in node_ids
    }
    responses = {
        node_id: [
            response["properties"]["choice"]
            for response in db.get_choices_for_node(node_id)
        ]
        for node_id in node_ids
    }
    response_locations = {
        node_id: [
            response["target"]
            for response in db.get_choices_for_node(node_id)
        ]
        for node_id in node_ids
    }

    START = "forest hut"
    ENDS = ["forest exit"]
    entry_points = [
        CommandHandler("start", adventure_step(
            START,
            ENDS,
            descriptions[START],
            responses[START]
        ))
    ]
    states = {
        node_id: [
            MessageHandler(
                filters.Regex(response),
                adventure_step(
                    location,
                    ENDS,
                    descriptions[location],
                    responses[location]
                )
            )
            for response, location in zip(responses[node_id], response_locations[node_id])
        ]
        for node_id in node_ids
    }

    application.add_handler(ConversationHandler(
        entry_points=entry_points,
        states=states,
        fallbacks=[],
    ))

    application.run_polling()


if __name__ == "__main__":
    main()
