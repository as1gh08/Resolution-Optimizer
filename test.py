import pyautogui
from resolution_optimizer import ResolutionOptimizer

ro = ResolutionOptimizer((1920, 1280))
pyautogui.moveTo(ro.calculate_current(pixel_cord=(200, 1000))) #pixel_cord=(200, 1000) will find required pixel in other resolution


