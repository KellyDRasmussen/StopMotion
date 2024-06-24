# stop_motion.py
# Read Bluetooth Remote Shutter
# from /dev/input/event5 and /dev/input/event6
# filter for key down of ENTER and VOLUMNUP

from evdev import InputDevice, categorize, ecodes
import asyncio
import os
from datetime import datetime
import shutil
from picamera import PiCamera

# Define your input devices
Shutter5 = InputDevice('/dev/input/event5')
Shutter6 = InputDevice('/dev/input/event6')

# Initialize the Pi camera
pi_cam = PiCamera()

EV_VAL_PRESSED = 1
KEY_ENTER = 28
KEY_VOLUMNUP = 115

print(Shutter5)
print(Shutter6)
print('=== Start ===')

# Function to capture image from Lifecam HD-6000 using fswebcam
def capture_image_lifecam():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/path/to/save/lifecam/images/img_{timestamp}.jpg'  # Placeholder for Lifecam file path
    os.system(f'fswebcam -r 1280x720 --no-banner {file_path}')
    shutil.move(file_path, f'/path/to/simple/gallery/directory/img_{timestamp}.jpg')
    print(f'Lifecam image saved to {file_path}')

# Function to capture image from Pi Zero camera using picamera
def capture_image_pi_cam():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/path/to/save/picam/images/img_{timestamp}.jpg'  # Placeholder for Pi Cam file path
    pi_cam.capture(file_path)
    shutil.move(file_path, f'/path/to/simple/gallery/directory/img_{timestamp}.jpg')
    print(f'Pi Cam image saved to {file_path}')

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


