# Daily Mail Report Bot

[简体中文](https://github.com/chenbinghan666/mail_digest_bot/blob/main/README.md) · **English** · [日本語](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.pt.md)

Groups sample emails by sender and sends a daily report to Telegram. This was my first public Python project. Start with the report builder and the Telegram client to see how it works.

Python · Telegram Bot API

## Features

- Read local configuration from `.env`.
- Count the total number of sample emails and the number of emails from each sender.
- Send the report to the specified Telegram chat.

## Install and run

1. Run `python -m pip install -r requirements.txt` to install dependencies.
2. Copy `.env.example` to `.env` and fill in the following configuration.

   ```dotenv
   BOT_NAME=daily_mail_report_bot
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

3. Run `python main.py` to generate and send the report.

Please keep `.env` containing Bot Token on this machine.

## Report example

```text
Yesterday Mail Report

Total emails: 3

Top senders:
boss@example.com - 2 emails
client@example.com - 1 emails
```

## Source files

- `main.py` strings together the entire process.
- `config.py` loads configuration.
- `report_builder.py` generates reports.
- `telegram_client.py` sends report.

The current version uses sample data. Follow-up exploration directions include Microsoft Graph email reading, scheduled sending and email importance judgment.
