# Daily Mail Report Bot

[简体中文](https://github.com/chenbinghan666/mail_digest_bot/blob/main/README.md) · [English](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.en.md) · [日本語](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.ja.md) · **Deutsch** · [Français](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.pt.md)

Gruppiert Beispiel-E-Mails nach Absender und sendet einen Tagesbericht an Telegram. Mein erstes öffentliches Python-Projekt trennt die Berichtserstellung vom Nachrichtenversand.

Python · Telegram Bot API

## Funktion

- Lokale Konfiguration von `.env` lesen.
- Zählen Sie die Gesamtzahl der Beispiel-E-Mails und die Anzahl der E-Mails von jedem Absender.
- Senden Sie den Bericht an den angegebenen Telegram-Chat.

## Installieren und ausführen

1. Führen Sie `python -m pip install -r requirements.txt` aus, um Abhängigkeiten zu installieren.
2. Kopieren Sie `.env.example` nach `.env` und füllen Sie die folgende Konfiguration aus.

   ```dotenv
   BOT_NAME=daily_mail_report_bot
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

3. Führen Sie `python main.py` aus, um den Bericht zu generieren und zu senden.

Bitte bewahren Sie `.env` mit dem Bot-Token auf diesem Computer auf.

## Beispielbericht

```text
Yesterday Mail Report

Total emails: 3

Top senders:
boss@example.com - 2 emails
client@example.com - 1 emails
```

## Code-Eingabe

- `main.py` reiht den gesamten Prozess aneinander.
- `config.py` lädt die Konfiguration.
- `report_builder.py` generiert Berichte.
- `telegram_client.py` sendet Bericht.

Die aktuelle Version verwendet Beispieldaten. Zu den weiteren Erkundungsanweisungen gehören das Lesen von Microsoft Graph-E-Mails, das geplante Senden und die Beurteilung der E-Mail-Wichtigkeit.
