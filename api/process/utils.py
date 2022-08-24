import numpy as np

def decode_one_hot(oh_vector):
    oh_vector = np.array(oh_vector)
    return np.where(oh_vector==1)