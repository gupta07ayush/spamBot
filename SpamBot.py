#this python program sends the compliment.txt file content
#line by line at the target(whatsapp chat)

import random
import time
import pyautogui as pt
time.sleep(5)
file=open("compliment.txt", 'r')
file=list(file)

random.shuffle(file)

for word in file:
    time.sleep(0)
    pt.typewrite(word)
    pt.press("enter")


