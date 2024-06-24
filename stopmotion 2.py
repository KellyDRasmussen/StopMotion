# stop_motion.py
# Read Bluetooth Remote Shutter
# from /dev/input/event5 and /dev/input/event6
# filter for key down of ENTER and VOLUMNUP

from evdev import InputDevice, categorize, ecodes
import asyncio
import cv2
import os
from datetime import datetime
import shutil

# Define your input devices
Shutter5 = InputDevice('/dev/input/event5')
Shutter6 = InputDevice('/dev/input/event6')

# Define your cameras
lifecam = cv2.VideoCapture(0)  # Lifecam HD-6000, adjust the index if needed
pi_cam = cv2.VideoCapture(1)   # Pi Zero camera, adjust the index if needed

EV_VAL_PRESSED = 1
KEY_ENTER = 28
KEY_VOLUMNUP = 115

print(Shutter5)
print(Shutter6)
print('=== Start ===')

# Function to capture image from Lifecam HD-6000
def capture_image_lifecam():
    ret, frame = lifecam.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f'/path/to/save/lifecam/images/img_{timestamp}.jpg'  # Placeholder for Lifecam file path
        cv2.imwrite(file_path, frame)
        shutil.move(file_path, '/path/to/simple/gallery/directory/img_{timestamp}.jpg')
        print(f'Lifecam image saved to {file_path}')
    else:
        print('Failed to capture image from Lifecam')

# Function to capture image from Pi Zero camera
def capture_image_pi_cam():
    ret, frame = pi_cam.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f'/path/to/save/picam/images/img_{timestamp}.jpg'  # Placeholder for Pi Cam file path
        cv2.imwrite(file_path, frame)
        shutil.move(file_path, '/path/to/simple/gallery/directory/img_{timestamp}.jpg')
        print(f'Pi Cam image saved to {file_path}')
    else:
        print('Failed to capture image from Pi Cam')

async def print_events(device):
    async for event in device.async_read_loop():
        if event.type == ecodes.EV_KEY and event.value == EV_VAL_PRESSED:
            if event.code == KEY_ENTER:
                print('<ENTER> Pressed')
                capture_image_lifecam()
            elif event.code == KEY_VOLUMNUP:
                print('<VOLUMNUP> Pressed')
                capture_image_pi_cam()
            print(device.path, categorize(event), sep=': ')
            print('---')

for device in Shutter5, Shutter6:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()

# Release the cameras when done
lifecam.release()
pi_cam.release()
cv2.destroyAllWindows()

