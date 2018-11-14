import subprocess

command = "C:/ffmpeg/bin/ffmpeg.exe -i C:/Users/Lukas/Desktop/POM_Dataset/new_dataset/females/Lukas.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)