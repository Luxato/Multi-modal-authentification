import json
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from decimal import Decimal
import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import cv2
import keras.models
import re
import sys
from pprint import pprint
from load import *
import time
# Custom methods
from classifier_speaker import speaker_classifier
from classifier_face import face_classifier
from fuzzy_logic import get_fusion_face_voice_accuracy

app = Flask(__name__)
cors = CORS(app)

app.debug = True
global model, graph

DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\'


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    with open('C:\\wamp64\\www\\Multi-modal-authentification\\data2.json') as f:
        data = json.load(f)

    voice = data['voice']['path']
    image = data['image']

    voice_data = speaker_classifier("C:\\wamp64\\www\\Multi-modal-authentification\\" + voice)

    voice_person = voice_data['voice_results']['label']
    voice_probability = voice_data['voice_results']['probability']

    face_data = face_classifier(image)

    face_person = face_data['face_results']['label']
    face_probability = face_data['face_results']['probability']

    fused_probability = get_fusion_face_voice_accuracy(float(face_probability), float(voice_probability) * 100, 0)

    # log to file
    timestr = time.strftime("%Y%m%d-%H%M%S")

    with open("fused_probabilities.log", "a") as myfile:
        myfile.write(
            timestr + "_facelabel_" + face_person + "_faceacc_" + face_probability + "_voiceacc_" + str(float(voice_probability) * 100)
            + "_voicelabel_" + voice_person + "_fusionacc_" + str(fused_probability) + "\n"
        )

    return fused_probability


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
