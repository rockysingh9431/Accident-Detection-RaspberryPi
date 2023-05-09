import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import time
from buzzer import buzzerApp
from api import apiApp
model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX

def startapplication():
    video = cv2.VideoCapture("cars.mp4") # for camera use video = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if(pred == "Accident"):
            prob = (round(prob[0][0]*100, 2))
            
        # #to beep when alert:
            if(prob > 90):
                apiApp()
                buzzerApp()

            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred + " " + str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            return
        cv2.imshow('Video', frame)  

if __name__ == '__main__':
    startapplication()
