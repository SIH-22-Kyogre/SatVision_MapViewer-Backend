import pickle
import os
import numpy as np

from . import utils

PICKLES_PATH = os.path.join(
    os.path.abspath(os.path.split(__file__)[0]),
    os.path.pardir,
    'assets',
    'pickles'
)

classifier_mapping = {
    "vgg16-eurosat": "vgg16_classifier_eurosat.pkl"
}


def classify_image(img, clf_name):
    
    model = pickle.load(open(os.path.join(
        PICKLES_PATH, 
        classifier_mapping.get(clf_name, None)
    ), 'rb'))

    if model is not None:
        pred_class = model.predict(
            np.expand_dims(img, axis=0)
        )[0]
        return int(utils.decode_one_hot(pred_class))

    else:
        return -1
    
