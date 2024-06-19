# stop_motion.py
# Read Bluetooth Remote Shutter
# from /dev/input/event5 and /dev/input/event6
# filter for key down of ENTER and VOLUMNUP

from evdev import InputDevice, categorize, ecodes
import asyncio
import cv2
from datetime import datetime

# Define your camera and input devices
Shutter5 = InputDevice('/dev/input/event5')
Shutter6 = InputDevice('/dev/input/event6')
camera = cv2.VideoCapture(0)  # Change the index if needed

EV_VAL_PRESSED = 1
EV_VAL_RELEASED = 0
KEY_ENTER = 28
KEY_VOLUMNUP = 115

print(Shutter5)
print(Shutter6)
print('=== Start ===')

# Function to capture image
def capture_image():
    ret, frame = camera.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f'/path/to/save/images/img_{timestamp}.jpg'  # Placeholder for file path
        cv2.imwrite(file_path, frame)
        print(f'Image saved to {file_path}')
    else:
        print('Failed to capture image')

async def print_events(device):
    async for event in device.async_read_loop():
        if event.type == ecodes.EV_KEY and event.value == EV_VAL_PRESSED:
            if event.code == KEY_ENTER:
                print('<ENTER> Pressed')
                capture_image()
            elif event.code == KEY_VOLUMNUP:
                print('<VOLUMNUP> Pressed')
                capture_image()
            print(device.path, categorize(event), sep=': ')
            print('---')

for device in Shutter5, Shutter6:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()

# Release the camera when done
camera.release()
cv2.destroyAllWindows()
