from config import load_config
from telegram_client import send_message
from report_builder import build_report

def main():
    config=load_config()
    token=config["telegram_bot_token"]
    chat_id=config["telegram_chat_id"]
    emails = [
    {
        "sender": "boss@example.com",
        "subject": "Project deadline",
        "summary": "Please send the report before Friday.",
    },
    {
        "sender": "client@example.com",
        "subject": "Meeting follow-up",
        "summary": "The client asked for updated pricing details.",
    },
]
    digest=build_report(emails)
    text=digest
    send_message(token,chat_id,text)
    
    

if __name__=="__main__":
    main()
