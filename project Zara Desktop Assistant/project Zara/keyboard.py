from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller() #Controller() creates an object named keyboard, allowing control over keyboard inputs.

def volumeup(): #This function simulates pressing the volume up key on the keyboard five times.
    for i in range(5):  #Each press and release of Key.media_volume_up increases the system volume.
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)