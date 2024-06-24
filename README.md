# Stop Motion Rig

This project sets up a stop-motion rig using a Raspberry Pi, a Lifecam HD-6000, and a Bluetooth remote as the trigger.

## Setup

### Prerequisites

1. **Hardware:**
   - Raspberry Pi
   - Lifecam HD-6000
   - Bluetooth Remote

2. **Software:**
   - Python 3.5+
   - Required Python packages (listed in `requirements.txt`)

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

3. Ensure you have the necessary permissions to access `/dev/input/event*` devices and write to the specified directory.

### Running the Script

1. Connect your Bluetooth remote to the Raspberry Pi.
2. Run the script:

    ```sh
    python stop_motion.py
    ```

3. Press the `ENTER` or `VOLUMEUP` button on the remote to capture images.

### Customization

- Update the file path in `stop_motion.py` to the directory where you want to save the images:

    ```python
    file_path = f'/path/to/save/images/img_{timestamp}.jpg'
    ```

## Resources

- [Python evdev documentation](https://python-evdev.readthedocs.io/en/latest/tutorial.html)
- [Lifecam HD-6000 setup](https://www.bot-thoughts.com/2013/01/lifecam-hd-6000-autofocus-fix-raspberry.html)
- [Raspberry Pi live cam setup](https://healeycodes.com/raspberry-pi-live-cam)
