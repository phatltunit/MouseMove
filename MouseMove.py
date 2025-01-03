import mouse 
import time
import random
import keyboard
from threading import Thread
import sys
from screeninfo import get_monitors



def move(right, bottom, back):
    right = right if back == False else -right
    bottom = bottom if back == False else - bottom
    mouse.move(right,bottom, absolute= False, duration=1)

def move_action(min_range, max_range,time):
    map = generate_map(min_range, max_range, time)
    for m in map:
        print(print_log(m[0],m[1]))
        move(m[0],m[1],False)
    while len(map) > 0:
        back = map.pop()
        print(print_log(back[0],back[1]))
        move(back[0], back[1],True)

def print_log(x,y):
    horizontal = 'right' if x > 0 else 'left'
    vertical = 'bottom' if y > 0 else 'top'
    return "Move to {horizontal} {x} pixels, {vertical} {y} pixels".format(horizontal=horizontal, x=abs(x), vertical=vertical, y=abs(y))

def generate_map(min_range, max_range,time):
    count =  0
    result = []
    monitor = get_monitors()[0]
    mouse_position = mouse.get_position()
    current_x = mouse_position[0]
    current_y = mouse_position[1]
    while count < time:
        random_range_right = random.randint(min_range,max_range)
        random_range_bottom = random.randint(min_range,max_range)
        new_x = current_x + random_range_right
        new_y = current_y + random_range_bottom
        if new_x > monitor.width or new_x < 0 or new_y > monitor.height or new_y < 0:
            continue
        else:
            result.append([random_range_right, random_range_bottom])
            count += 1
    return result

    

def run():
    while True:
        min_range = -200
        max_range = 200
        min_time = 5
        max_time = 10
        random_time = random.randint(1,5)
        move_action(min_range, max_range, random_time)
        keyboard.send('alt')
        sleep_time = random.randint(min_time,max_time)
        print('Sleeping for {time} seconds'.format(time=sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':
    thread = Thread(target=run)
    thread.daemon = True
    thread.start()
    print("Mouse move is running")
    keyboard.wait('esc')
    print('Quit program')
    sys.exit()