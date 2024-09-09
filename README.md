# Circle-collection-bot

**Circle-collection-bot** is a Telegram bot that allows users to send video messages (circles), and the bot will analyze them and try to detect cats. There may be more to this bot than meets the eye 🤫.

## Features

- The bot accepts video messages (circles) from users.
- Circles are uploaded to a local server.
- The bot uses an object detection model (YOLO) to determine if the video message contains cats (or other objects).
- The user receives a response with the analysis results: "Cats detected!" or "No cats found."

## Technologies Used

- **Aiogram**: An asynchronous library for working with the Telegram Bot API.
- **YOLO (You Only Look Once)**: An object detection model used for analyzing video messages.
- **Python**: The main programming language used.
