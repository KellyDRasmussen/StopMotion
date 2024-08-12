import pygame
import os
from time import sleep
from picamera import PiCamera
import subprocess

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Stop Motion")

# Initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)

# Create a directory to store images
output_dir = "stop_motion"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set initial variables
running = True
image_count = 0

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Take a picture on spacebar press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                image_count += 1
                image_path = os.path.join(output_dir, f"frame_{image_count:03d}.jpg")
                camera.capture(image_path)
                print(f"Captured {image_path}")
                sleep(0.5)  # Small delay to avoid multiple captures

            # Exit on ESC press
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Update display (could add a preview later)
    screen.fill((255, 255, 255))  # white background
    pygame.display.flip()

# Clean up
camera.close()
pygame.quit()

# Create a video from the captured images using ffmpeg
video_name = os.path.join(output_dir, "stop_motion_video.mp4")
subprocess.run([
    "ffmpeg", "-framerate", "10", "-i", os.path.join(output_dir, "frame_%03d.jpg"),
    "-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p", video_name
])

print("Done! Images saved to", output_dir)
print(f"Video created: {video_name}")
