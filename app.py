from flask import Flask, render_template, request

import keras.models
import re
import sys
import os

#sys.path.append(os.path.abspath('./model'))
from load import *

app = Flask(__name__)
app.debug = True
global model, graph

print(app.root_path)
#app.root_path = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = 'C:\\wamp64\\www\\Multi-modal-authentification\\'

# TODO helper functions

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # TODO get the face and voice
    # TODO preprocess them
    # TODO fuse the probabilities with fusion
    # TODO return results as json
    pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
