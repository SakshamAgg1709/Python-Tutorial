# Making A Bot to attend School classes

import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetid, meetpass):
    #Opens Up Zoom
    subprocess.call('C:\Admin\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(10)
    #Join the meeting
    join_in = pyautogui.locateCenterOnScreen('D:\Zoom Join button.png')
    pyautogui.moveTo(join_in)
    pyautogui.click()




sign_in(4976252482, 1265255)