import keyboard
from keyboard import KeyboardEvent
import json
import sys
import threading
from datetime import datetime
from os.path import expanduser
import os

class Log():
    def __init__(self, name, type):
        self.name = name
        self.type = type
    

LOG_FOLDER = expanduser('~') + '/log/'
OUTPUT = LOG_FOLDER + 'keyboard.log'
def from_keyboard_to_file():
    print('Listening for keyboard')
    result = keyboard.record(until= 'enter')
    file = open(OUTPUT, 'a')
    list = []
    for event in result:
        map_event_to_json(event, list)
    file.writelines(list)

def map_event_to_json(event:KeyboardEvent, list:list):
    time = datetime.now()
    list.append(time.strftime("%Y-%m-%d %H:%M:%S") + "[KeyboardEvent]: " + json.dumps(Log(event.name, event.event_type).__dict__)+ "\n")

def main():
    if not(os.path.exists(LOG_FOLDER)):
        os.makedirs(LOG_FOLDER)
    while True:
        from_keyboard_to_file()

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.daemon = True
    thread.start()
    print('Starting keyboard recording...')
    keyboard.wait('')
    print('Quit program')
    sys.exit()
    
