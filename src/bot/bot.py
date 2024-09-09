import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ContentType
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

DOWNLOAD_FOLDER = 'video_notes/'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Скинь кружёк")


@dp.message_handler(content_types=ContentType.VIDEO_NOTE)
async def handle_video_note(message: types.Message):
    video_note = message.video_note

    if video_note:
        file_info = await bot.get_file(video_note.file_id)
        file_path = file_info.file_path

        file_name = f"{DOWNLOAD_FOLDER}{video_note.file_id}.mp4"

        await bot.download_file(file_path, file_name)

        await message.reply(f"Кружок сохранён")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
