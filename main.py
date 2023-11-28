import pyautogui
import keyboard
import time

while not keyboard.is_pressed('q'):
    try:
        obrazek = pyautogui.locateOnScreen('accept.png', confidence=.7)
        center_x = obrazek.left + obrazek.width /2
        center_y = obrazek.top + obrazek.height /2
        pyautogui.click(center_x,center_y)
        time.sleep(1)
        print("Poszlo...")

    except:
        time.sleep(1)
        print("Czekam...")