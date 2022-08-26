import pickle
import os
import numpy as np
import keras
import tensorflow as tf
import torch
from PIL import Image

from . import utils
import timm
from torch import nn

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
    # VGG16
    ND_MODEL_PATH = r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\api\\assets\\pickles\\vgg16_eurosat.h5"
    KD_MODEL_PATH = "/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/api/assets/pickles/vgg16_classifier_eurosat.pkl"

    # for effv0
    ND_MODEL_PATH = r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\api\\assets\\pickles\\model4.bin"

    # for VGG16 - comment otherwise
    # model = pickle.load(open(KD_MODEL_PATH, 'rb')) #KD
    # model = tf.keras.models.load_model(ND_MODEL_PATH) #ND

    # if model is not None:
    #     img = Image.fromarray(img).resize((64, 64))
    #     pred_class = model(
    #         np.expand_dims(img, axis=0)
    #     )[0]
    #     return int(utils.decode_one_hot(pred_class))

    # else:
    #     return -1

    # for effv0

    def make_efficientv0_classifier():

        config = {'lr':5e-5,
            'wd':1e-2,
            'bs':64,
            'img_size':256,
            'nfolds':5,
            'epochs':20,
            'num_workers':4,
            'seed':1000,
            'model_name':'tf_efficientnet_b0',
            }

        classes = ['AnnualCrop', 'HerbaceousVegetation', 'PermanentCrop',
        'Industrial', 'Pasture', 'Highway', 'Residential', 'River',
        'SeaLake', 'Forest']

        num_classes = len(classes)


        class Model(nn.Module):
            def __init__(self,model_path,pretrained=True):
                super(Model,self).__init__()
                self.backbone = timm.create_model(model_path,pretrained=pretrained)
                in_features = self.backbone.classifier.in_features
                self.backbone.classifier = nn.Linear(in_features,128)
                self.dropout = nn.Dropout(0.2)
                self.relu = nn.ReLU()
                self.layer = nn.Linear(128, num_classes)

            def forward(self,x):
                x = self.relu(self.backbone(x))
                x = self.layer(self.dropout(x))
                return x
        
        model = Model("efficientnet_b0")
        model.load_state_dict(open(ND_MODEL_PATH, 'rb'))

        return model

    # model = torch.load(open(ND_MODEL_PATH, 'rb'))
    # model = make_efficientv0_classifier()
    # model.eval()
    # print(model(np.expand_dims(img, axis=0)))


    def make_resnet152v2_classifier():

        import tensorflow as tf
        from keras.models import Model
        # from keras.applications import VGG16, VGG19

        ND_MODEL_FILE = "D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\api\\assets\\pickles\\ResNet152V2.h5"
        KD_MODEL_FILE = "/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/api/assets/pickles/base_classification.h5"
        model = tf.keras.models.load_model(KD_MODEL_FILE)
        return model

    model = make_resnet152v2_classifier()
    if model is not None:
        img = Image.fromarray(img).resize((64, 64))
        print(model.predict(np.expand_dims(img, axis=0)))
        return np.argmax(model.predict(np.expand_dims(img, axis=0))[0])

    
    
