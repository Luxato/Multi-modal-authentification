# inspired by https://www.youtube.com/watch?v=PmZ29Vta7Vc

import os
from PIL import Image
import numpy as np

from os import listdir
from os.path import isfile, join

import cv2

import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()

DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\dataset\\faces\\'

label_ids = {}

x_train = [];
x_labels = [];

current_id = 0
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        frame_count = 0;
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            # print(file)
            label = file.split("_")[0]
            frame_count = file.split("_")[1].split(".")[0]
            if int(frame_count) >= 25:  # Take just 25 frame, leave 5 for validation
                continue
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            # Then get ROI of the image
            x_train.append(image_array)
            x_labels.append(id_)

print(label_ids)

recognizer.train(x_train, np.array(x_labels))
recognizer.save("./faces_model.yml")

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)
