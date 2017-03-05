import win32api
import random

"""
Author: CZMoodyDev
Notes: Simple script to prevent your computer from sleeping without
changing system preferences. (It's just a simple cursor mover)
"""

def mouseMove():
    x_pos = random.randint(1, 250)
    y_pos = random.randint(1, 250)
    win32api.SetCursorPos((x_pos, y_pos))