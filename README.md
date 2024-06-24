# Stop Motion Rig

This project sets up a stop-motion rig using a Raspberry Pi, a Lifecam HD-6000, and a Bluetooth remote as the trigger.

## Setup

### Prerequisites

1. **Hardware:**
   - Raspberry Pi
   - Lifecam HD-6000
   - Pi Zero camera
   - Bluetooth Remote

2. **Software:**
   - Python 3.5+
   - Required Python packages (listed in `requirements.txt`)
   - `fswebcam` utility

### Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/KellyDRasmussen/StopMotion.git
    cd StopMotion
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Install `fswebcam`:

    ```sh
    sudo apt-get install fswebcam
    ```

4. Ensure you have the necessary permissions to access `/dev/input/event*` devices and write to the specified directory.

### Running the Script

1. Connect your Bluetooth remote to the Raspberry Pi.
2. Run the script:

    ```sh
    python stop_motion.py
    ```

3. Press the `ENTER` button to capture an image with the Lifecam HD-6000.
4. Press the `VOLUMEUP` button to capture an image with the Pi Zero camera.

### Customization

- Update the file paths in `stop_motion.py` to the directories where you want to save the images:

    ```python
    file_path = f'/path/to/save/lifecam/images/img_{timestamp}.jpg'
    file_path = f'/path/to/save/picam/images/img_{timestamp}.jpg'
    ```

- Update the shared directory for moving the images to a location accessible by the Simple Gallery app:

    ```python
    shutil.move(file_path, '/path/to/simple/gallery/directory/img_{timestamp}.jpg')
    ```

## Resources

- [Python evdev documentation](https://python-evdev.readthedocs.io/en/latest/tutorial.html)
- [Lifecam HD-6000 setup](https://www.bot-thoughts.com/2013/01/lifecam-hd-6000-autofocus-fix-raspberry.html)
- [Raspberry Pi live cam setup](https://healeycodes.com/raspberry-pi-live-cam)
- [fswebcam documentation](http://manpages.ubuntu.com/manpages/bionic/man1/fswebcam.1.html)
- [picamera documentation](https://picamera.readthedocs.io/en/release-1.13/)
