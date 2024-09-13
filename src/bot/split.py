import av
from io import BytesIO

def split_video_to_frames(video_data, fps=5):
    if isinstance(video_data, BytesIO):
        video_data.seek(0)
    else:
        raise TypeError("Expected a BytesIO object")

    container = av.open(video_data)
    
    stream = container.streams.video[0]
    stream_time_base = stream.time_base
    video_fps = stream.average_rate

    frame_interval = int(video_fps // fps)

    frames = []
    for i, frame in enumerate(container.decode(video=0)):
        if i % frame_interval == 0:
            frame_rgb = frame.to_image().convert('RGB')
            frames.append(frame_rgb)
    
    container.close()
    return frames