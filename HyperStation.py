import ctypes
import time
from ctypes import wintypes
from screen_brightness_control import get_brightness, set_brightness
import cv2

class HyperStation:
    def __init__(self):
        self.huser32 = ctypes.WinDLL('user32', use_last_error=True)
        self.gwl_exstyle = -20
        self.ws_ex_layered = 0x00080000
        self.ws_ex_transparent = 0x00000020
        self.set_layered_window_attributes = self.huser32.SetLayeredWindowAttributes
        self.set_layered_window_attributes.argtypes = [wintypes.HWND, wintypes.COLORREF, wintypes.BYTE, wintypes.DWORD]
        self.set_layered_window_attributes.restype = wintypes.BOOL

    def get_ambient_light(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            cap.release()
            raise RuntimeError("Unable to capture video frame for ambient light detection.")
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_light_intensity = int(gray.mean())
        cap.release()
        return avg_light_intensity

    def adjust_brightness_and_contrast(self):
        ambient_light = self.get_ambient_light()
        print(f"Ambient Light Intensity: {ambient_light}")

        brightness = max(10, min(100, ambient_light))
        print(f"Setting brightness to: {brightness}")

        set_brightness(brightness)

    def start(self):
        try:
            while True:
                self.adjust_brightness_and_contrast()
                time.sleep(10)  # Adjust every 10 seconds
        except KeyboardInterrupt:
            print("HyperStation stopped.")


if __name__ == "__main__":
    hyperstation = HyperStation()
    hyperstation.start()