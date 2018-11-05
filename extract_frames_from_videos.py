# This script takes a video and extracts 30 frames which contains faces
# One time run script to prepare dataset for training.

import os
import cv2
import random

from face_detection import find_face

# Path to the dataset.
directory = "C:\\Users\\Lukas\\Desktop\\POM_Dataset\\new_dataset\\males" # Switch between males and females.

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if os.path.isdir(os.path.join(directory, filename)):
        continue

    if filename.endswith(".mp4"):
        print("Now video " + filename + " is being processed.")
        tmp = filename.split('.')
        directory_name = tmp[0]
        if not os.path.exists(os.path.join(directory, directory_name)):
            # Create directories for every person.
            os.makedirs(os.path.join(directory, directory_name))

    # Get the video number of frames.
    cap = cv2.VideoCapture(os.path.join(directory, filename))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    success, image = cap.read()

    # Save frames into the array for easier access.
    frames = []
    while success:
        frames.append(image)
        success, image = cap.read()
    cap.release()

    count = 0
    iterator = 1
    random_frames = set()
    while iterator <= 30:
        new_random_num = random.randint(0, length - 1)
        if new_random_num in random_frames:
            continue
        else:
            face = find_face(frames[new_random_num])
            if face is not 0:
                random_frames.add(new_random_num)
                cv2.imwrite(
                    os.path.join(os.path.join(directory, directory_name), str(directory_name) + "_%d.jpg") % iterator,
                    face)
                iterator += 1
            else:
                print("Alert: No face found!")