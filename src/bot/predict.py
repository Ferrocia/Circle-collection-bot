import os

from ultralytics import YOLO
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from dotenv import load_dotenv

load_dotenv()
storage = RedisStorage2()

model = YOLO(os.getenv('Path_to_yolo'))
model = YOLO(os.getenv('Path_to_best'))


def predictImage(frames):
    results = model(frames)
    points = 0
    for result in results:
        predicted_class_index = result.probs.top1
        predicted_class_name = model.names[predicted_class_index]
        confidence = result.probs.top1conf
        print(f"Предсказанный класс: {predicted_class_name} с уверенностью {confidence}")
        if predicted_class_name == 'cats':
            points += 1

    return points


async def add_points(user_id, points):
    user_scores = await storage.get_data(user=user_id)

    if 'points' not in user_scores:
        user_scores['points'] = 0

    user_scores['points'] += points

    await storage.set_data(user=user_id, data=user_scores)

    return user_scores['points']
