import sys
sys.path.append('/user/local/lib/python2.7/site-packages')

import cv2
import numpy as np
from twilio.rest import Client 

account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token)

cap = cv2.VideoCapture(0)
key = ''
balls = False
sent = 1

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green color
    low_green = np.array([15, 35, 133])
    high_green = np.array([60, 175, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)


    cv2.imshow("Frame", frame)
    cv2.imshow("Green", green)
    for i in green:

        ratio_brown = cv2.countNonZero(green_mask)/(green.size/3)
        ratio = np.round(ratio_brown*100, 2)
        if ratio < 15:
            if sent == 1:
                print("No Balls")
                sent = 0
                message = client.messages.create( 
                              from_='',  
                              body='NO BALLS LEFT IN THE DRIVING RANGE',      
                              to='' 
                          )

        else:
            sent = 1


    key = cv2.waitKey(1)
    if key == 27:
        break
