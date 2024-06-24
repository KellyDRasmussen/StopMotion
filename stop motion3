import tkinter as tk
from picamera import PiCamera
from datetime import datetime
import os

# Initialize the cameras
pi_cam = PiCamera()

# Function to capture image from Pi Camera
def capture_image_pi_cam():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/path/to/save/picam/images/img_{timestamp}.jpg'  # Placeholder for Pi Cam file path
    pi_cam.capture(file_path)
    print(f'Pi Cam image saved to {file_path}')

# Function to capture image from Lifecam HD-6000 using fswebcam
def capture_image_lifecam():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/path/to/save/lifecam/images/img_{timestamp}.jpg'  # Placeholder for Lifecam file path
    os.system(f'fswebcam -r 1280x720 --no-banner {file_path}')
    print(f'Lifecam image saved to {file_path}')

# Define key press event handlers
def on_key_press(event):
    if event.char == 'p':  # Press 'p' to capture from Pi Camera
        capture_image_pi_cam()
    elif event.char == 'l':  # Press 'l' to capture from Lifecam
        capture_image_lifecam()

# Create the tkinter window
root = tk.Tk()
root.title("Camera Control Interface")
root.geometry("300x200")

# Instructions label
label = tk.Label(root, text="Press 'p' for Pi Camera\nPress 'l' for Lifecam HD-6000", font=("Helvetica", 16))
label.pack(pady=20)

# Bind the key press event
root.bind("<KeyPress>", on_key_press)

# Start the tkinter main loop
root.mainloop()

# Clean up the camera when done
pi_cam.close()
