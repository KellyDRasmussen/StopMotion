import os
import time
import subprocess
from picamera import PiCamera
from pynput import keyboard

# Set up the camera
camera = PiCamera()
camera.resolution = (1024, 768)

# Directory to save images
image_dir = 'images'
os.makedirs(image_dir, exist_ok=True)

image_count = 0

def on_press(key):
    global image_count
    try:
        if key.char == 'c':  # Press 'c' to capture
            image_path = os.path.join(image_dir, f'image_{image_count:03d}.jpg')
            camera.capture(image_path)
            print(f'Captured {image_path}')
            image_count += 1
    except AttributeError:
        pass

def create_video():
    output_video = 'animation.mp4'
    ffmpeg_command = [
        'ffmpeg', '-framerate', '10', '-i', os.path.join(image_dir, 'image_%03d.jpg'),
        '-c:v', 'libx264', '-r', '30', '-pix_fmt', 'yuv420p', output_video
    ]
    subprocess.run(ffmpeg_command)
    print(f'Video saved as {output_video}')

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    print("Press 'c' to capture an image. Press 'Esc' to finish and create the video.")
    listener.join()

# After capturing images, compile them into a video
create_video()
