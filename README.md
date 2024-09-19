# Circle-collection-bot
This project is a Telegram bot that allows users to play a game where they send video notes, and the bot detects how many frames in the video contain cats. The more cats detected, the higher the user's score.

## Features
YOLO V8 for image classification to detect cats in video frames.
Telegram bot built using the Aiogram library.
Redis for storing user scores.
Installation
Clone this repository:

`https://github.com/Ferrocia/Circle-collection-bot.git`

## Set up your environment variables. Create a .env file in the root directory and add the following variables:
```
TOKEN=your_telegram_bot_token
Path_to_yolo=path_to_your_yolo_model
Path_to_best=path_to_your_trained_yolo_model
```
You can train the model on your dataset using the following command inside the main.py file:

`model.train(data="Path to dataset folder/", epochs=100, imgsz=80)`

## How It Works
Video Splitting: When the bot receives a video note, it splits the video into frames. The function split_video_to_frames() in split.py handles this.

Image Classification: The frames are passed to the YOLO model to classify each frame and count the number of cat detections. The function predictImage() in predict.py performs this task.

Points Calculation: For each frame classified as a cat, the user earns a point. These points are stored in Redis.

Bot Interaction: Users interact with the bot by sending a video note. The bot processes the video, predicts how many frames contain a cat, and sends the user their score.

## How to Run bot
Start the bot by running:

`python bot.py`

Interact with the bot by sending a video note in Telegram. The bot will process the video and respond with your cat detection score.


