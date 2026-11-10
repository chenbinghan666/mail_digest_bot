# Daily Mail Report Bot

[简体中文](https://github.com/chenbinghan666/mail_digest_bot/blob/main/README.md) · **English** · [日本語](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.pt.md)

## Project overview

Groups sample emails by sender and sends a daily report to Telegram. This was my first public Python project. Start with the report builder and the Telegram client to see how it works.

Python · Telegram Bot API

## Project links

[Full documentation in Chinese](https://github.com/chenbinghan666/mail_digest_bot/blob/main/README.md) · [@chenbinghan666](https://github.com/chenbinghan666/chenbinghan666/blob/main/docs/locales/README.en.md)

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
