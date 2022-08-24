import pickle

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
    
    model = pickle.load(os.path.join(
        PICKLES_PATH, 
        classifier_mapping.get(clf_name, None)
    ))

    if model is not None:
        return model.predict(
            np.asarray(img).expand_dims(axis=0)
        )[0]

    else:
        return -1
    
