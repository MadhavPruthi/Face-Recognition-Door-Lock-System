import fnmatch
import os

import cv2
import numpy as np

import config

from PIL import Image

def train_classifier():
    
    print("Reading training images...")

    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Using prebuilt frontal face training model, for face detection
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Get the faces and IDs
    faces,ids = getImagesAndLabels('dataset', detector)

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    recognizer.write('trainer/trainer.yml')
    print("Training Done")
                

# Create method to get the images and label data
def getImagesAndLabels(path, detector):

    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    # Initialize empty face sample
    faceSamples=[]
    
    # Initialize empty id
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x,y,w,h) in faces:

            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])

            # Add the ID to IDs
            ids.append(id)

    # Pass the face array and IDs array
    return faceSamples,ids







