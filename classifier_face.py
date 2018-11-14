from get_face_roi import find_face
import cv2
import pickle
from PIL import Image
import numpy as np
from get_face_roi import find_face

DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\'

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("faces_model.yml")

labels = {}

with open("labels.pickle", 'rb') as f:
    original_labels = pickle.load(f)
    # Reverse dictionary lookup
    labels = {v: k for k, v in original_labels.items()}

# print(original_labels)
# print(labels)

def face_classifier(image):
    image_array = cv2.imread(DATA_DIR + image, 0)

    #image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # if (find_face(image_array) != False):
    #     image_array = find_face(image_array)


    id_, conf = recognizer.predict(image_array)

    print("Confidence is " + str(100 - conf))
    print(labels[id_])

    final_predictions = {}
    final_predictions['face_results'] = {
        "label": labels[id_],
        "probability": str(100 - conf)
    }

    return final_predictions



