# inspired by https://www.youtube.com/watch?v=PmZ29Vta7Vc


import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


# Returns either face from the image or false when there is no face.
def find_face(image):
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.5, minNeighbors=5)

    is_face = False
    for (x, y, w, h) in faces:
        #roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]
        is_face = True

    if is_face:
        return roi_color
    else:
        return False
