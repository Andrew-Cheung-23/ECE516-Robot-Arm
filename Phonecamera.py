import serial.tools.list_ports

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import os
import time

def check_picture_exists(folder_path, picture_name):
    # Construct the full path to the picture file
    picture_path = os.path.join(folder_path, picture_name)
    print(picture_path)
    
    # Check if the file exists
    if os.path.exists(picture_path):
        return True
    else:
        return False

def find_red_pixels(image):
    # Define lower and upper bounds for red color in HSV
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        return image,True
    return image,False




cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

cap2 = cv2.VideoCapture(1)
if not cap2.isOpened():
    print("Error: Unable to open camera.")
    exit()
ports = serial.tools.list_ports
serialInst = serial.Serial()

portVar = "COM" + str(3)
serialInst.baudrate =  9600
serialInst.port = portVar
serialInst.open()

numleds = 20

pattern = ""
output_dir = 'captured_frames'
os.makedirs(output_dir, exist_ok=True)



Finished = "finish"

frame_count = 0
count = -1

ret, frame = cap.read()

totaleframes = -1


folder_path = "Camera"
os.makedirs(folder_path, exist_ok=True)

while True:
    
    message = input("Enter message to send to Arduino: ") 
        
    if(message == "exit"):
        exit()
    elif(message == "next"):
        for i in range(numleds):
            serialInst.write(message.encode('utf-8'))
            count = count +1
            totaleframes= totaleframes+1
            picture_name = "frame_" + str(totaleframes)+ ".jpg"
            
            while(True):
                if(check_picture_exists(folder_path, picture_name)):
                    print(picture_name + " is here")
                    image_path = os.path.join(folder_path, picture_name)
                    phoneframe = cv2.imread(image_path)
                    break
                else:
                    #print( picture_name)
                    time.sleep(2)
                
            
            
            processedframe, hi = find_red_pixels(phoneframe)
            cv2.imshow('Red Pixels Detection', processedframe)
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if(hi):
                pattern = pattern + str(1)
            else:
                pattern = pattern + str(0)
        serialInst.write(pattern.encode('utf-8'))
        count = 0
        pattern = ""
        time.sleep(2)

        ret, frame = cap.read()
        
        frame_filename = os.path.join(output_dir, f'frame_{frame_count}.jpg')
        frame_count = frame_count +1
        cv2.imwrite(frame_filename, frame)
        

            
    elif(message == "pattern"):
        print(pattern)
    elif(message == "swap"):
        cap, cap2 = cap2, cap
    elif(message == "camera"):
        ret, frame = cap.read()
        
        frame_filename = os.path.join(output_dir, f'frame_{frame_count}.jpg')
        frame_count = frame_count +1
        cv2.imwrite(frame_filename, frame)
        

        
