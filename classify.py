import train
import cv2
import config
import numpy as np
import os

import datetime
import time

def load_data():
    
    train.train_classifier()

    #Load training data into model
    print('Loading training data...')
    
    # Create Local Binary Patterns Histograms for face recognization
    model = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained mode
    model.read('trainer/trainer.yml')
    
    return model



def classify(model):
    
    recognizer = model
    
    # Load prebuilt model for Frontal Face
    cascadePath = "haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    cam = cv2.VideoCapture(0)
    

    while True:
        # Read the video frame
        ret, im =cam.read()
        
        
        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Display the video frame with the bounded rectangle
        cv2. imshow('Recogniser', im)
            

        if cv2.waitKey(10) & 0xFF == ord('q'):
            
            cam.release()
            cv2.destroyAllWindows()
            
            if len(faces):
            
                # Recognize the face belongs to which ID
                Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
                if confidence < config.POSITIVE_THRESHOLD:
                    recognized = True
                    print("Welcome ", Id)
                else:
                    recognized = False
                
                with open('logs/log.txt','a') as file:
                    file.write("Date and Time: " + str(datetime.datetime.now()) + " Probable ID: " + str(Id) + " Confidence: " + str(confidence) + " Recognized: " + str(recognized) + " Image Location: logs/Images/" + str(datetime.datetime.now()) + ".jpg\n")
                    
                cv2.imwrite("logs/Images/" + str(datetime.datetime.now()) + ".jpg", im)
                
                print("Confidence predicted: " ,confidence)
                               
                return recognized
            
            else:
                
                print("No faces Detected")
                return False
