# import string
# from time import sleep
# import cv2
# import easyocr
# import firebase_admin
# from firebase_admin import db
# from firebase_admin import credentials
# import datetime
# import imutils
# import numpy as np

# cred = credentials.Certificate("plaka_admin_sdk.json")
# firebase_admin.initialize_app(cred, {
#   'databaseURL': 'https://plaka-e9d0b-default-rtdb.firebaseio.com'
# })
# ref = db.reference('/')
# registered = ref.child('Registered')
# unregistered = ref.child('Unregistered')
# logs = ref.child('Logs')

# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error opening webcam!")
#     exit()

# reader = easyocr.Reader(['en'], gpu=False)
# x = datetime.datetime.now()
# str_date = x.strftime("%Y-%m-%d-%H:%M:%S")

# interval = 0
# seconds = 60

# while True:
#     interval = interval + 1
#     ret, frame = cap.read()
#     if cv2.waitKey(1) == ord('q'):
#         break
#     if not ret:
#         print("Failed to capture frame!")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('Webcam Feed', gray)
#     if interval > seconds:
#         text = reader.readtext(gray)
#         d = registered.get()
#         interval = 0
#         for t in text:
#             bbox, text, score = t
#             if score > 0.50:
#                 text = text.translate(str.maketrans('', '', string.punctuation))
#                 text = text.strip()
#                 if len(text) < 9:
#                     text = text[:8]
#                     print(text.upper())
#                 # count = 0
#                 # for i in d.values():
#                 #     count += 1
#                 #     if text == i:
#                 #         logs.push({
#                 #         str_date : 'REGISTERED - ' + text.upper(),
#                 #         })
#                 #         print("MATCH")
#                 #         break
#                 #     elif text != i and count == len(d):
#                 #         logs.push({
#                 #         str_date : 'UNREGISTERED - ' + text.upper(),
#                 #         })
#                 #         print("NO MATCH")

import string
from datetime import datetime
from time import sleep
import cv2
import easyocr
import firebase_admin
from easyocr import Reader
from firebase_admin import db
from firebase_admin import credentials
import datetime

from firebase_admin.credentials import Certificate

cred: Certificate = credentials.Certificate("plaka_admin_sdk.json")
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://plaka-e9d0b-default-rtdb.firebaseio.com'
})
ref = db.reference('/')
registered = ref.child('Registered')
unregistered = ref.child('Unregistered')
logs = ref.child('Logs')

cap = cv2.VideoCapture(1)

if cap.isOpened():
    pass
else:
    print("Error opening webcam!")
    exit()

reader: Reader = easyocr.Reader(['en'], gpu=False)
x: datetime = datetime.datetime.now()
str_date: str = x.strftime("%Y-%m-%d-%H:%M:%S")

interval: int = 0
seconds: int = 60

while True:
    interval = interval + 1
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('q'):
        break
    if not ret:
        print("Failed to capture frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Webcam Feed', gray)
    if interval > seconds:
        text = reader.readtext(gray)
        d = registered.get()
        interval = 0
        for t in text:
            bbox, text, score = t
            if score > 0.50:
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = text.strip()
                print(text.upper())
                # count = 0
                # for i in d.values():
                #     count += 1
                #     if text == i:
                #         logs.push({
                #         str_date : 'REGISTERED - ' + text.upper(),
                #         })
                #         print("MATCH")
                #         break
                #     elif text != i and count == len(d):
                #         logs.push({
                #         str_date : 'UNREGISTERED - ' + text.upper(),
                #         })
                #         print("NO MATCH")