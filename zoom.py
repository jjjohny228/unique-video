import os
from moviepy.editor import VideoFileClip


def zoom(input_file, output_file, zoom_factor=1.2):
    # Load the video clip
    clip = VideoFileClip(input_file)
    clip = clip.rotate(-1)

    # Calculate the dimensions for zooming
    zoom_width = int(clip.w / zoom_factor)
    zoom_height = int(clip.h / zoom_factor)
    zoom_x = (clip.w - zoom_width) // 2
    zoom_y = (clip.h - zoom_height) // 2

    # Crop the clip to zoom
    zoomed_clip = clip.crop(x1=zoom_x, y1=zoom_y, x2=zoom_x + zoom_width, y2=zoom_y + zoom_height)

    # Resize the cropped clip back to the original size
    final_clip = zoomed_clip.resize(newsize=(clip.w, clip.h))

    # Write the modified clip to a new file
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

source_folder = 'source'
result_folder = 'result'

# Получаем список всех файлов в папке source
files = os.listdir(source_folder)
# Проходим по каждому файлу в папке source
for file in files:
    # Формируем полные пути к исходному и результирующему файлам
    input_file_path = os.path.join(source_folder, file)
    output_file_path = os.path.join(result_folder, file)

    # Вызываем функцию для изменения метаданных и raw_header
    zoom(input_file_path, output_file_path)