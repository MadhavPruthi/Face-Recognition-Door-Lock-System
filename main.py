import os
import time
import sys
import RPi.GPIO as GPIO

import config
import classify
import face_datasets

import servo
import train

locked = True

print("Initializing .. Wait.. ")

try:
    
    model= classify.load_data()
    
except:
    
    print("Training DataSet is Empty!! Let's Start by adding an entry")
    face_datasets.detection()
    train.train_classifier()
    
door = servo.Door()
door.lock()
print("--------Welcome to Raspi Facetech------------")


while True:
    
    print("----------------------------------")
    print("1: Enter new Authorised person")
    print("2: Scan Image")
    print("3: Re-Train Model")
    print("4: Exit")
    print("----------------------------------")

    choice=input("Enter your choice: ")

    if choice=="1":
        
        print("Kindly keep your face in front of camera and avoid other person's intrustion while training")
        face_datasets.detection()
        train.train_classifier()
        
        
    elif choice=="2":
        
        print("Recognize Face Command is pressed")
        
        recognized = classify.classify(model)

        if recognized:
            if locked == True:
                print("Unlock")
                locked = False
                door.unlock()
                time.sleep(3)
                door.lock()

            print("The door is unlocked")

        else:
            
            if locked == False:
                locked = True
                door.lock()
                time.sleep(0.01)
                
            print("Recognize agian!")
        
    elif choice == "3":
        
        train.train_classifier()
        
    elif choice == "4":
        
        break
    
    else:
        print("Invalid Entry")
