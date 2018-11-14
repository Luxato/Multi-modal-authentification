import numpy as np
import librosa
from sklearn.preprocessing import LabelBinarizer
import json


from os import listdir
from os.path import isfile, join

from keras.models import model_from_json

from keras import backend as K


def speaker_classifier(path_to_recording):
    DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\dataset\\voices\\'

    files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

    X_train = []
    X_val = []
    for i in range(0, len(files)):
        tmp = files[i].split("_")[0]
        if tmp == "left":
            X_train.append(files[i])
        else:
            X_val.append(files[i])

    labels = []
    for i in range(len(X_train)):
        label = X_train[i].split('_')[1].split('.')[0]
        if label not in labels:
            labels.append(label)
    # print(labels)

    max_length = 1305

    label_binarizer = LabelBinarizer()
    label_binarizer.fit(list(set(labels)))


    def prepare(path):
        wave, sr = librosa.load(path, mono=True)
        mfcc = librosa.feature.mfcc(wave, sr)
        mfcc = np.pad(mfcc, ((0, 0), (0, max_length - len(mfcc[0]))), mode='constant', constant_values=0)
        return np.array(mfcc)


    with open("C:\\wamp64\\www\\Multi-modal-authentification\\" + './model.json', 'r') as f:
        model = model_from_json(f.read())

    model.load_weights(
        "C:\\wamp64\\www\\Multi-modal-authentification\\" + 'checkpoints/speaker_recognition_model_08.hdf5')

    # model = tf.keras.models.load_model("./checkpoints_old/voice_recognition_best_model_05.hdf5")



    data = prepare(path_to_recording)
    # data = np.reshape(data, data.shape + (1,))
    # X = np.array(data)

    b = data.reshape(-1, data.shape[0], data.shape[1])

    # print(b.shape)


    prediction = model.predict(b)
    # prediction = model.predict_classes(b, batch_size=32, verbose = 2)
    # print(prediction[0][1])
    index = False
    highest_probability = False
    final_predictions = {}
    final_predictions['predictions'] = {}
    final_predictions['results'] = {}
    for i in range(0, len(prediction[0])):
        final_predictions['predictions'][labels[i]] = str(prediction[0][i])
        if prediction[0][i] > highest_probability:
            highest_probability = prediction[0][i]
            index = i

    # print("Highest probability is " + str(highest_probability))
    # print(labels[index])

    final_predictions['voice_results'] = {
        "label": labels[index],
        "probability": str(highest_probability)
    }

    #json_data = json.dumps(final_predictions)

    K.clear_session()

    #print(json_data)
    return final_predictions
