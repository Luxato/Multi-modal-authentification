# inspired by https://www.youtube.com/watch?v=PmZ29Vta7Vc


import numpy as np
import cv2
import pickle



face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

# Gets image as
# Returns either face from the image or false when there is no face.
def find_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    if not faces:
        return 0

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    return roi_color

image = cv2.imread("I:\\POM-dataset\\new_dataset\\females\\Emma\\frame.jpg")

cv2.imshow('image',find_face(image))
cv2.waitKey(0)
cv2.destroyAllWindows()
