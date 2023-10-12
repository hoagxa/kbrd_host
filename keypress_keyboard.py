#https://www.delftstack.com/howto/python/python-detect-keypress/#detect-keypress-using-the-keyboard-module-in-python
#pip3 install keyboard
#chmod +x keypress_keyboard.py
# sudo python3 keypress_keyboard.py

import keyboard

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        break
    
while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
    
keyboard.on_press_key("r", lambda _:print("You pressed r"))