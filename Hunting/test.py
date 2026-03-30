import time
from pynput.keyboard import Key, Controller
# import functions as fn
# import cv2

kb = Controller()

def square():
    kb.press('d')
    time.sleep(0.5)
    kb.press('s')
    time.sleep(0.5)
    kb.press('q')
    time.sleep(0.5)
    kb.press('z')
    time.sleep(0.5)

#Switching tabs and getting to Desmume
with kb.pressed(Key.cmd_r):
    kb.press(Key.tab)
    kb.release(Key.tab)
    
time.sleep(2)

with kb.pressed(Key.alt_l):
    kb.press(Key.tab)
    kb.release(Key.tab)

time.sleep(2)

cpt = 0

with kb.pressed(Key.space):
    while cpt < 1000000000:
        square()
        i += 1

    time.sleep(1)
    print("FIN")