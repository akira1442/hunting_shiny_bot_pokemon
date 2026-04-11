import time
from pynput.keyboard import Key, Controller
import pyautogui
# import functions as fn
# import cv2

kb = Controller()

def square():
    
    pyautogui.keyDown("d")
    time.sleep(0.01)
    pyautogui.keyUp("d")
    
    pyautogui.keyDown("s")
    time.sleep(0.01)
    pyautogui.keyUp("s")
    
    pyautogui.keyDown("q")
    time.sleep(0.01)
    pyautogui.keyUp("q")
    
    pyautogui.keyDown("z")
    time.sleep(0.01)
    pyautogui.keyUp("z")


#Switching tabs and getting to Desmume
# with pyautogui.press("alt"):
#     kb.press(Key.tab)
    # kb.release(Key.tab)

# with kb.pressed(Key.alt_l):
#     kb.press(Key.tab)
#     kb.release(Key.tab)

print("Debut du test dans 1 sec")
time.sleep(1)

cpt = 0

pyautogui.hotkey("alt", "tab")

pyautogui.keyDown("space")
while cpt < 10:
    square()
    cpt += 1
    
pyautogui.keyUp("space")
time.sleep(1)
print("FIN")