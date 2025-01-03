import math
import mouse
import keyboard
import sys

def move_action(min_range, max_range,time):
    radius = 100 
    for i in range(time):
        angle = 2 * math.pi * i / time
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        print("Move to ({}, {})".format(x, y))
        # Perform the actual movement
        mouse.move(x, y, absolute= False, duration= 1)

if __name__ == "__main__":
    move_action(0, 100, 360)
    keyboard.wait("esc")
    print("Quit program")
    sys.exit()