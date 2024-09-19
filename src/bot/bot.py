import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ContentType
from dotenv import load_dotenv
from io import BytesIO
from predict import predictImage, add_points
from split import split_video_to_frames

load_dotenv()

TOKEN = os.getenv('TOKEN_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Скинь кружёк")


@dp.message_handler(content_types=ContentType.VIDEO_NOTE)
async def handle_video_note(message: types.Message):
    chat_id = message.chat.id
    print(chat_id)
    print('asad')
    video_note = message.video_note

    if video_note:
        file_info = await bot.get_file(video_note.file_id)
        file_path = file_info.file_path

        video_data = BytesIO()

        await bot.download_file(file_path, video_data)
        print(file_path)
        video_data.seek(0)
        frames = split_video_to_frames(video_data)
        predic = predictImage(frames)
        points = await add_points(chat_id, predic)
        await bot.send_message(chat_id, f'Cat scores {points}')
        print(f"Кружок сохранён в переменную, размер видео {video_data.getbuffer().nbytes} байт.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
