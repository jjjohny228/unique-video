import moviepy.editor as mp
import subprocess
import datetime
from uuid import uuid4
from moviepy.editor import *


def change_video(input_path, output_path, overlay_path):
    """Uniqalizes a video by removing metadata, adjusting speed, mirroring,
       rotating, and overlaying an image.

    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the uniqalized video.
        overlay_path (str): Path to the PNG image for overlay.
    """

    print(f"Uniqalizing video: {input_path}")

    # Open the video with metadata removal
    clip = mp.VideoFileClip(input_path)

    # Reduce speed to 1.1x
    # clip = clip.speedx(2)

    # Rotate by 1 degree
    clip = clip.rotate(1)

    # Mirror the video
    # clip = clip.fx(vfx.mirror_x)

    # Load and resize overlay image (if provided)
    if overlay_path:
        overlay = (mp.ImageClip(overlay_path).set_duration(clip.duration))

        # Create a composite video with the overlay
        clip = CompositeVideoClip([clip, overlay])

    # Write the uniqalized video to the output path
    clip.write_videofile(output_path, codec='libx264')
    print(f"Uniqalized video saved: {output_path}")


def change_metadata(input_file, output_file, video_metadata=None, audio_metadata=None, raw_header=True):
    ffmpeg_command = [
        'C:\\ffmpeg\\bin\\ffmpeg.exe',
        '-y',
        '-i',
        input_file,  # Путь к выходному файлу
    ]

    # Add video metadata
    if video_metadata:
        for key, value in video_metadata.items():
            ffmpeg_command.extend(['-metadata:s:v', f'{key}={value}'])

    # Add audio metadata
    if audio_metadata:
        for key, value in audio_metadata.items():
            ffmpeg_command.extend(['-metadata:s:a', f'{key}={value}'])

    ffmpeg_command.extend(['-c:v', 'copy', '-c:a', 'copy', output_file])

    # Run ffmpeg command
    subprocess.run(ffmpeg_command)


# Example usage
source_folder = "source"
result_folder = "result"
overlay_image_path = "overlay.png"  # Optional
metadata = {
        'title': uuid4(),
        'artist': uuid4(),
        'album': uuid4(),
        'creation_time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000000Z')
    }

video_metadata = {
    'title': uuid4(),
    'comment': uuid4(),
    'creation_time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000000Z')
}
audio_metadata = {
    'artist': uuid4(),
    'comment': uuid4(),
    'creation_time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000000Z')
}

# uniqalize_video(input_video_path, output_video_path, overlay_image_path)

# Получаем список всех файлов в папке source
files = os.listdir(source_folder)
# Проходим по каждому файлу в папке source
for file in files:
    # Формируем полные пути к исходному и результирующему файлам
    input_file_path = os.path.join(source_folder, file)
    output_file_path = os.path.join(result_folder, file)

    # Вызываем функцию для изменения метаданных и raw_header
    change_metadata(input_file_path, output_file_path, video_metadata, audio_metadata)
