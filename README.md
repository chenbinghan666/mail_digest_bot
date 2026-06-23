# Daily Mail Report Bot

A beginner-friendly Python automation project that builds a daily email report
from sample email data and sends it to Telegram.

This is my first Python project prepared for GitHub. The current version uses
sample email data so the project can run without Outlook API setup.

## Features

- Reads private settings from a `.env` file
- Builds a daily email report from sample email data
- Counts total emails
- Counts emails by sender
- Sends the report to Telegram

## Project Structure

```text
mail_digest_bot/
  main.py
  config.py
  telegram_client.py
  report_builder.py
  requirements.txt
  .env.example
  .gitignore
  README.md
```

## Setup

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```text
BOT_NAME=daily_mail_report_bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

Do not upload your `.env` file to GitHub because it contains private keys.

## Run

```bash
python main.py
```

## Example Report

```text
Yesterday Mail Report

Total emails: 3

Top senders:
boss@example.com - 2 emails
client@example.com - 1 emails
```

## Future Improvements

- Fetch real Outlook emails using Microsoft Graph
- Send the report automatically every day
- Add AI-based email importance detection
