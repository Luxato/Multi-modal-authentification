import os
import cv2
import sys
import random

from face_detection import find_face


# Path to the dataset.
directory = "I:\\POM-dataset\\new_dataset\\females"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    if os.path.isdir(os.path.join(directory, filename)):
        continue
    
    if filename.endswith(".mp4"): 
        tmp = filename.split('.')
        directory_name = tmp[0]       
        if not os.path.exists(os.path.join(directory, directory_name)):            
            # Create directories for every person.
            os.makedirs(os.path.join(directory, directory_name))
    
    # Get the video number of frames.
    cap = cv2.VideoCapture(os.path.join(directory, filename))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    success,image = cap.read()
    
    
    # Generate random unique numbers in interval <0, number_of_frames>
    random_frames = set()
    while len(random_frames) < 30:
        random_frames.add(random.randint(0, length))
    
    #print(os.path.join(directory, "frame.jpg"))
    #cv2.imshow('image',image)
    
    count = 0
    while success:
        if (count in random_frames):
            print(os.path.join(os.path.join(directory, directory_name), str(directory_name) + "_%d.jpg") % count)
            # TODO if there is a face then save it.

            # TODO if there is no face, generate a random number which is not in the set and try it on that frame as well.
        #cv2.imwrite(os.path.join(os.path.join(directory, directory_name), "frame%d.jpg") % count, image)
        success,image = cap.read()
        count += 1
    
    
    #print(os.path.join(os.path.join(directory, directory_name), "frame.jpg"))
    #cv2.imwrite(os.path.join(os.path.join(directory, directory_name), "frame.jpg"), image)
    cap.release()
    
    
    #cv2.destroyAllWindows()

    
    
    
    # TODO remember saved frames
    # TODO If there is a face then save the image into the person's dir.
    