# Daily Mail Report Bot

[简体中文](https://github.com/chenbinghan666/mail_digest_bot/blob/main/README.md) · [English](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.en.md) · [日本語](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/mail_digest_bot/blob/main/docs/locales/README.es.md) · **Português**

Agrupa e-mails de exemplo por remetente e envia um relatório diário ao Telegram. Meu primeiro projeto público em Python separa a geração do relatório do envio das mensagens.

Python · Telegram Bot API

## Função

- Leia a configuração local de `.env`.
- Conte o número total de e-mails de amostra e o número de e-mails de cada remetente.
- Envie o relatório para o chat do Telegram especificado.

## Instalar e executar

1. Execute `python -m pip install -r requirements.txt` para instalar dependências.
2. Copie `.env.example` para `.env` e preencha a seguinte configuração.

   ```dotenv
   BOT_NAME=daily_mail_report_bot
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

3. Execute `python main.py` para gerar e enviar o relatório.

Por favor, mantenha `.env` contendo Bot Token nesta máquina.

## Exemplo de relatório

```text
Yesterday Mail Report

Total emails: 3

Top senders:
boss@example.com - 2 emails
client@example.com - 1 emails
```

## Entrada de código

- `main.py` encadeia todo o processo.
- `config.py` carrega configuração.
- `report_builder.py` gera relatórios.
- `telegram_client.py` envia relatório.

A versão atual usa dados de amostra. As instruções de exploração de acompanhamento incluem leitura de e-mail do Microsoft Graph, envio programado e avaliação da importância do e-mail.
