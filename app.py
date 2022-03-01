import base64
import io
from tensorflow.keras import layers
#import tensorflow_hub as hub

import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from flask import Flask
from flask import request
from flask_cors import CORS
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
