import os
import redis
import cv2
import numpy as np

VpxFrameKey = "udp_vpx_frames"

r = redis.Redis('localhost', 6379)

frame_width = 320
frame_height = 240

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for i in range(0, 80):
    frameBuf = r.lindex(VpxFrameKey, i)
    frame = np.zeros(frame_width, dtype=np.uint8)
    for h in range(0, frame_height):
        frameTmp = np.frombuffer(frameBuf, dtype=np.uint8, count = frame_width, offset = frame_width * h)
        frame = np.row_stack((frame, frameTmp))
    frame = np.delete(frame, 0, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_YUV2GRAY_420)

    face_reg = True
    try: 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    except :
        print("no face reg")
        face_reg = False
    if face_reg :
        for(x,y,w,h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        
    cv2.imshow("frame", frame)
    cv2.waitKey(10)


