# Stop Motion Rig

This project sets up a stop-motion rig using a Raspberry Pi Zero W, a ZeroCam, and a keyboard as the trigger.

## Setup

### Prerequisites

1. Hardware:
    * Raspberry Pi Zero W
    * Pi Zero Camera
    * Keyboard

2. Software:
    * Python 3.5+
    * Required Python packages (listed in `requirements.txt`)
    * `ffmpeg` utility

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/KellyDRasmussen/StopMotion.git
    cd StopMotion
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install `ffmpeg`:
    ```bash
    sudo apt-get install ffmpeg
    ```

### Running the Script

1. Run the stop motion script:
    ```bash
    python stop_motion.py
    ```

2. Press the `Spacebar` key to capture an image with the ZeroCam.

3. Press the `Esc` key to finish capturing and compile the images into a video.

### Automating Image Compilation

After capturing the images, the script automatically compiles them into a video using `ffmpeg`.

### Customization

* Update the directory where images are saved in `stop_motion.py` if needed:
    ```python
    output_dir = 'stop_motion'
    ```

* Adjust camera settings as needed within the script:
    ```python
    camera.resolution = (1024, 768)
    ```

## Resources

* [Python picamera documentation](https://picamera.readthedocs.io/)
* [Pygame documentation](https://www.pygame.org/docs/)
* [ffmpeg documentation](https://ffmpeg.org/documentation.html)
