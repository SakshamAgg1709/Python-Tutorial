import subprocess
import pyautogui
import time
import keyboard
import pandas as pd
from datetime import datetime
import pyscreeze

def sign_in(meetingid,password):
    """
    Opens up the zoom app
    change the path specific to your computer
    """
    subprocess.call('C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    time.sleep(15)
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(4)


    # Type the meeting ID
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click(meeting_id_btn)
    pyautogui.write(meetingid)

    # Hits the join button
    join_btn2 = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn2)
    pyautogui.click(join_btn2)
    time.sleep(5)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click(meeting_pswd_btn)
    pyautogui.write(password)
    pyautogui.press('enter')

# sign_in("497 625 2482","compsc")

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]

        m_id = str(row.iloc[0, 1])
        m_pswd = str(row.iloc[0, 2])

        sign_in(m_id, m_pswd)
        time.sleep(40)
        print('Signed in')

