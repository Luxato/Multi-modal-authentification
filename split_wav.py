from pydub import AudioSegment
import os


directory = "./dataset/voices/"
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)

    person = filename.split('.')[0]

    newAudio = AudioSegment.from_wav("./dataset/voices/" + filename)
    newAudio = newAudio[0:30000]
    newAudio.export("./dataset/voices/left_" + person + ".wav", format="wav")

    newAudio = AudioSegment.from_wav("./dataset/voices/" + filename)
    newAudio = newAudio[30000:60000]
    newAudio.export("./dataset/voices/right_" + person + ".wav", format="wav")
