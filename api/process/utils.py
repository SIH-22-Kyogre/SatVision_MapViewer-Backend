import numpy as np

def decode_one_hot(oh_vector):
    return np.argmax(oh_vector)