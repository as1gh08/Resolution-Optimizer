from typing import Optional
import ctypes

class ResolutionOptimizer:
    def __init__(self, input_resolution: tuple):
        self.input_resolution = input_resolution
        self.current_resolution = self.get_resolution()

    def get_resolution(self) -> Optional[tuple]:
        try:
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            return screensize
        except Exception as ex:
            print(f"Error while getting the screen resolution: {ex}")
            return None

    def calculate(self, target_resolution: tuple, pixel_cord: tuple, round_res: bool = True) -> Optional[tuple]:
        if sum(self.input_resolution) < sum((640, 480)) or sum(target_resolution) < sum((640, 480)):
            print("The minimal resolution must be (640x480)")
            return None
        try:
            target_w, target_h = target_resolution
            input_w, input_h = self.input_resolution

            pixel_w, pixel_h = pixel_cord

            pixel_w = pixel_w / (input_w / target_w)
            pixel_h = pixel_h / (input_h / target_h)

            return (round(pixel_w), round(pixel_h)) if round_res else (pixel_w, pixel_h)

        except Exception as ex:
            print("Error, recheck the resolution values")
            return None

    def calculate_current(self, pixel_cord: tuple, round_res: bool = True):
        if sum(self.input_resolution) < sum((640, 480)):
            print("The minimal resolution must be (640x480)")
            return None
        try:
            target_w, target_h = self.current_resolution
            input_w, input_h = self.input_resolution

            pixel_w, pixel_h = pixel_cord

            pixel_w = pixel_w / (input_w / target_w)
            pixel_h = pixel_h / (input_h / target_h)

            return (round(pixel_w), round(pixel_h)) if round_res else (pixel_w, pixel_h)

        except Exception as ex:
            print("Error, recheck the resolution values")
            return None 

