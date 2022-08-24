from flask import request
from flask_restful import Resource 
import base64 
import io 
import numpy as np
from PIL import Image

from ..process import classifier

# NOTE: Use reqparse instances for argument parsing from the URL - trigger it through the ctor

# TODO: Decide the req-res sequence for img_fetch-predict-render_class

class CoverClass(Resource):

    def __init__(self):
        pass

    def post(self, clf_name="vgg16-eurosat"):

        # POSTed 'img' data contains raw satellite image
        img_b64 = request.json.get('img')
        img_bytes = base64.b64decode(img_b64)
        img_np = np.asarray(Image.open(io.BytesIO(img_bytes)))

        pred_class = classifier.classify_image(img_np, clf_name)
        # TODO: Handle -1 error here?
        return pred_class
        
