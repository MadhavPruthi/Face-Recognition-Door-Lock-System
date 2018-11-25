# Import OpenCV2 for image processing
import cv2
import os

def detection():
    
    # For each person, one face id
    face_id = 0
    
    #Reading Current counter value from file
    with open('counter.txt', 'r') as file:
        face_id = int(file.read())
    
    with open('counter.txt', 'w') as file:
        file.write(str(face_id+1))

    # Start capturing video 
    vid_cam = cv2.VideoCapture(0)
    
    check, image_frame = vid_cam.read()
    
    
    # Detect object in video stream using Haarcascade Frontal Face
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Initialize sample face image
    count = 0
    clear = lambda: os.system('clear')
    
    # Start looping
    while(True):

        # Capture video frame
        _, image_frame = vid_cam.read()
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # Detect frames of different sizes, list of faces rectangles
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # Loops for each faces
        for (x,y,w,h) in faces:

            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            
            # Increment sample face image
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

         
        clear()
        print("counter: ", count)
            

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif count>300:
            break

    # Stop video
    vid_cam.release()

    # Close all started windows
    cv2.destroyAllWindows()
    
