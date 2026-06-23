import os

from dotenv import load_dotenv


def load_config():
    load_dotenv()

    return {"bot_name":os.getenv("BOT_NAME",""),
            "telegram_bot_token":os.getenv("TELEGRAM_BOT_TOKEN",""),
            "telegram_chat_id":os.getenv("TELEGRAM_CHAT_ID","")}
