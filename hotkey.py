import subprocess
from pynput import keyboard

# The key combination being used
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='e')},
    {keyboard.Key.shift, keyboard.KeyCode(char='E')}
]

# The currently active modifiers
pressed = set()

def execute():
    subprocess.call('python.exe firefoxScript.py') # excecutes the firefoxScript file as a different process


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        pressed.add(key)
        if any(all(k in pressed for k in COMBO) for COMBO in COMBINATIONS): 
            execute() #executes the script

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        pressed.discard(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
