# This code was inspired by book - Python Deep Learning Cookbook
# URL: https://www.packtpub.com/mapt/book/big_data_and_business_intelligence/9781787125193

# How to turn Tensorboard on to monitor training http://fizzylogic.nl/2017/05/08/monitor-progress-of-your-keras-based-neural-network-using-tensorboard/
# Command to execute: tensorboard --logdir=logs/

import numpy as np
import random
import librosa

from sklearn.preprocessing import LabelBinarizer

from keras.layers import LSTM, Dense, Dropout, Flatten
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
from matplotlib import pyplot

from os import listdir
from os.path import isfile, join

from time import time
from keras.callbacks import TensorBoard

DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\dataset\\voices\\'

files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

# print("Number of files is: " + str(len(files)))
# X_train, X_val = train_test_split(files, test_size=0.2, random_state=SEED)

X_train = []
X_val = []
for i in range(0, len(files)):
    tmp = files[i].split("_")[0]
    if tmp == "left":
        X_train.append(files[i])
    else:
        X_val.append(files[i])

# print('# Training examples: {}'.format(len(X_train)))
# print('# Validation examples: {}'.format(len(X_val)))


# print(len(X_train))
# print(X_train[0])
#
# print(len(X_val))
# print(X_val[0])

labels = []
for i in range(len(X_train)):
    label = X_train[i].split('_')[1].split('.')[0]
    if label not in labels:
        labels.append(label)
print(labels)

label_binarizer = LabelBinarizer()
label_binarizer.fit(list(set(labels)))


def one_hot_encode(x): return label_binarizer.transform(x)


n_features = 20
max_length = 1305
n_classes = len(labels)


def batch_generator(data, batch_size=16):
    # data is just the X_train
    while 1:
        random.shuffle(data)
        X, y = [], []
        for i in range(batch_size):
            wav = data[i]
            wave, sr = librosa.load(DATA_DIR + wav, mono=True)  # Adjust the path where the dataset is.
            label = wav.split('_')[1].split('.')[0]
            y.append(label)
            mfcc = librosa.feature.mfcc(wave, sr)
            mfcc = np.pad(mfcc, ((0, 0), (0, max_length - len(mfcc[0]))), mode='constant', constant_values=0)
            X.append(np.array(mfcc))
        yield np.array(X), np.array(one_hot_encode(y))


learning_rate = 0.001
batch_size = 32
n_epochs = 60
dropout = 0.8

input_shape = (n_features, max_length)
steps_per_epoch = 35

model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=input_shape,
               dropout=dropout))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(dropout))
model.add(Dense(n_classes, activation='softmax'))

opt = Adam(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

tensorboard = TensorBoard(log_dir="./logs/{}".format(time()))

model.summary()

callbacks = [ModelCheckpoint('checkpoints/speaker_recognition_model_{epoch:02d}.hdf5', save_best_only=True),
             EarlyStopping(monitor='val_acc', patience=2),
             tensorboard, ]

model.json = model.to_json()
with open("./model.json", "w") as json_file:
    json_file.write(model.json)

history = model.fit_generator(
    generator=batch_generator(X_train, batch_size),
    steps_per_epoch=steps_per_epoch,
    epochs=n_epochs,
    verbose=1,
    validation_data=batch_generator(X_val, 32),
    validation_steps=5,
    callbacks=callbacks
)

pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()
