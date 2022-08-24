import pickle


classifier_map = {
    "vgg16_eurosat": "vgg16_classifier_eurosat.pkl"
}


def classify_image(img, classifier):
    
    model = pickle.load(os.path.join(
        PICKLES_PATH, 
        classifier_map.get(classifier, None)
    ))

    if model is not None:
        return model.predict(
            np.asarray(img).expand_dims(axis=0)
        )[0]

    else:
        return -1
    
