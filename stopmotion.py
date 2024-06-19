# pyShutter.py
# Read Bluetooth Remote Shutter
# from /dev/input/event5 and /dev/input/event6
# filter for key down of ENTER and VOLUMNUP
#
# http://helloraspberrypi.blogspot.com/2020/06/detect-bluetooth-remote-shutter-ab.html
#
# Work on Python 3.5+
# For Reading events from multiple devices
# read https://python-evdev.readthedocs.io/en/latest/tutorial.html

from evdev import InputDevice, categorize, ecodes
import asyncio

Shutter5 = InputDevice('/dev/input/event5')
Shutter6 = InputDevice('/dev/input/event6')

EV_VAL_PRESSED = 1
EV_VAL_RELEASED = 0
KEY_ENTER = 28
KEY_VOLUMNUP = 115

print(Shutter5)
print(Shutter6)
print('=== Start ===')

async def print_events(device):
                
    async for event in device.async_read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == EV_VAL_PRESSED:
                if event.value == EV_VAL_PRESSED:
                    if event.code == KEY_ENTER:
                        print('<ENTER> Pressed')
                    elif event.code == KEY_VOLUMNUP:
                        print('<VOLUMNUP> Pressed')
                print(device.path, categorize(event), sep=': ')          
                print('---')

for device in Shutter5, Shutter6:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()

