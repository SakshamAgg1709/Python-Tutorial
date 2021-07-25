import subprocess
import pyautogui
from datetime import datetime
import time
import pyscreeze
import pandas as pd


"""pillow - install"""

def sign_in(meet_id, meet_pass):
    subprocess.call("C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(7)
    print("kndkcmd")


    join_btn = pyautogui.locateCenterOnScreen("join_button.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click(join_btn)
    time.sleep(5)
    print("Hi")
    meeting_id = pyautogui.locateCenterOnScreen("meeting_idbtn.png")
    pyautogui.moveTo(meeting_id)
    pyautogui.click(meeting_id)
    pyautogui.write(meet_id)

    join_btn2 = pyautogui.locateCenterOnScreen("join_btn2.png")
    pyautogui.moveTo( join_btn2)
    pyautogui.click( join_btn2)
    time.sleep(8)

    meeting_psw =  pyautogui.locateCenterOnScreen("meeting_pss.png")
    pyautogui.moveTo(meeting_psw)
    pyautogui.click(meeting_psw)
    pyautogui.write(meet_pass)
    pyautogui.press('enter')


sign_in("754 5731 2532","Kyx7rL")

df = pd.read_csv('schedule.csv')

while(True):
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]

        meet_id = str(row.iloc[0,1])
        meet_ps = str(row.iloc[0,2])
        sign_in(meet_id,meet_ps)
        time.sleep(20)
        print("Signed-In")
