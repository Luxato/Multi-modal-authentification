import os
import cv2
import random

from face_detection import find_face

# Path to the dataset.
directory = "I:\\POM-dataset\\new_dataset\\females"

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

    # Generate random unique numbers in interval <0, number_of_frames>
    random_frames = set()
    while len(random_frames) < 30:
        random_frames.add(random.randint(0, length))


    count = 0
    iterator = 1
    while success:
        if (count in random_frames):
            face = find_face(image)
            if face is not 0:
                cv2.imwrite(os.path.join(os.path.join(directory, directory_name), str(directory_name) + "_%d.jpg") % iterator, face)
                iterator += 1
            else:
                count = -1
                # No face found
                print("Alert: No face found!")
                while True:
                    new_random_num = random.randint(count + 1, length)
                    random_frames.discard(count)

                    if not new_random_num in random_frames:
                        random_frames.add(new_random_num)
                        break

        success, image = cap.read()
        count += 1

    cap.release()


