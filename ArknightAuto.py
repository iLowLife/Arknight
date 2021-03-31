import numpy as np
import cv2
import pyautogui
import time

#Grab desktop screen
from PIL import ImageGrab
from matplotlib import pyplot as plt

#prevent error
pyautogui.FAILSAFE = True 

#Declare image path
template_start = cv2.imread('template/template_start.png') #File path
template_start = cv2.cvtColor(template_start, cv2.COLOR_BGR2GRAY)

template_mission_start = cv2.imread('template/template_mission_start.png') #File path
template_mission_start = cv2.cvtColor(template_mission_start, cv2.COLOR_BGR2GRAY)

template_trust = cv2.imread('template/template_trust.png') #File path
template_trust = cv2.cvtColor(template_trust, cv2.COLOR_BGR2GRAY)

#Get Image Weith and Height
w_start, h_start = template_start.shape[::-1]
w_mission_start, h_mission_start = template_mission_start.shape[::-1]
w_trust, h_trust = template_trust.shape[::-1]

while(True):
    # Capture frame-by-frame
    img = ImageGrab.grab()
    img_np = np.array(img)

    # Convert screen to Gray for easy image processing
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    #Draw rectangle on screen
    res_template_start = cv2.matchTemplate(frame,template_start,cv2.TM_CCOEFF_NORMED)
    res_template_mission_start = cv2.matchTemplate(frame,template_mission_start,cv2.TM_CCOEFF_NORMED)
    res_template_trust = cv2.matchTemplate(frame,template_trust,cv2.TM_CCOEFF_NORMED)

    threshhold = 0.7

    location_start = np.where(res_template_start >= threshhold)
    #print(location_start)
    for pt in zip(*location_start[::-1]):
        x,y = pyautogui.position()
        if(x>0):
            print("Start Clicked")
        pyautogui.leftClick(pt)
        pyautogui.moveTo(x,y)
        cv2.rectangle(frame, pt, (pt[0] + w_start, pt[1] + h_start), (0,0,225), 2)
        time.sleep(2)
        break

    location_mission_start = np.where(res_template_mission_start >= threshhold)
   #print(location_mission_start)
    for pt in zip(*location_mission_start[::-1]):
        x,y = pyautogui.position()
        if(x>0):
            print("Mission Start Clicked")
        pyautogui.leftClick(pt)
        pyautogui.moveTo(x,y)
        cv2.rectangle(frame, pt, (pt[0] + w_mission_start, pt[1] + h_mission_start), (0,0,225), 2)
        time.sleep(2)
        break

    location_trust = np.where(res_template_trust >= threshhold)
    #print(location_trust)
    for pt in zip(*location_trust[::-1]):
        x,y = pyautogui.position()
        if(x>0):
            print("Mission Ended, Restarting Loop")
        pyautogui.leftClick(pt)
        pyautogui.moveTo(x,y)
        cv2.rectangle(frame, pt, (pt[0] + w_trust, pt[1] + h_trust), (0,0,225), 2)
        time.sleep(2)
        break

    # Display the resulting frame
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
