# HyperStation

HyperStation is a Python program designed to dynamically adjust the screen brightness and contrast of Windows devices based on ambient light conditions. By utilizing the device's camera to measure ambient light, HyperStation ensures an optimal viewing experience by automatically adjusting display settings.

## Features

- **Dynamic Adjustment**: Continuously monitors ambient light and adjusts screen brightness accordingly.
- **Automatic Optimization**: Ensures that screen settings are always optimized for current lighting conditions.
- **User-Friendly**: Runs in the background with minimal user intervention required.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` package)
- Screen Brightness Control (`screen-brightness-control` package)
- Windows operating system
- A functional webcam or camera

## Installation

1. Ensure Python 3.x is installed on your Windows system. You can download it from the [official Python website](https://www.python.org/).

2. Install the required Python packages using pip:

   ```bash
   pip install opencv-python screen-brightness-control
   ```

3. Download the `HyperStation.py` file from this repository.

## Usage

1. Open a command prompt and navigate to the directory containing the `HyperStation.py` file.

2. Run the script:

   ```bash
   python HyperStation.py
   ```

3. The program will start adjusting your screen brightness based on ambient light conditions. To stop the program, press `Ctrl+C`.

## Notes

- The program requires access to your computer's camera to measure ambient light. Ensure your webcam is functional and accessible.
- The adjustments are made every 10 seconds by default. This interval can be adjusted in the script by modifying the `time.sleep(10)` line.

## Disclaimer

This software is provided "as-is". The author is not responsible for any damage or data loss caused by the use of this program. Use it at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.