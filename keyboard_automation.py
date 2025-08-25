from pynput.keyboard import Key, Controller
import pyperclip
import time

keyboard = Controller()
time.sleep(3)

while True:
    time.sleep(0.2)
    mesaj = "Deneme!"
    pyperclip.copy(mesaj)

    with keyboard.pressed(Key.cmd):
        keyboard.press('v')
        time.sleep(0.1)
        keyboard.release('v')

    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(0.05)
    keyboard.release(Key.enter)