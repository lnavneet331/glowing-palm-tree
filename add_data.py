import pyautogui
import time
from tqdm import tqdm
import csv
import sys

time.sleep(2)
with open("data_clean.csv", newline="", encoding="cp1252") as file:
    data = csv.reader(file)
    raw = []
    for row in data:
        raw.append(row)
    
    for data in tqdm(raw):
        pyautogui.typewrite(data[0])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[1])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[3])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[8])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[4])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[9])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[11])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[5])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[10])
        #time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.typewrite(data[7])
        #time.sleep(0.2)
        pyautogui.press("tab")
        #time.sleep(0.1)
        pyautogui.press("tab")
        #time.sleep(0.1)
        pyautogui.press("tab")
        #time.sleep(0.1)
        #pyautogui.press("tab")
        #time.sleep(0.2)
        #pyautogui.press("enter")
        a = f"Eligibility Criteria: {data[2]}"
        pyautogui.typewrite(a)
        time.sleep(0.1)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(2)

"""
0. name -- 
1. provided by -- 
2. eligibility criteria -- 
3. scholarship amount --
4. link --
5. category
6. level
7. exam --
8. applivation type
9.type
"""