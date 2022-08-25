import pickle
import os
import numpy as np
import keras
import tensorflow as tf

from . import utils

PICKLES_PATH = os.path.join(
    os.path.abspath(os.path.split(__file__)[0]),
    os.path.pardir,
    'assets',
    'pickles'
)

# model = tf.keras.Model()


classifier_mapping = {
    "vgg16-eurosat": "vgg16_classifier_eurosat.pkl"
}


def classify_image(img, clf_name):
    ND_IMG_PATH = r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\api\\assets\\pickles\\vgg16_eurosat.h5"

    model = tf.keras.models.load_model(ND_IMG_PATH)

    if model is not None:
        pred_class = model.predict(
            np.expand_dims(img, axis=0)
        )[0]
        return int(utils.decode_one_hot(pred_class))

    else:
        return -1
    
