from flask import request
from flask_restful import Resource 

from ..process import classifier

# NOTE: Use reqparse instances for argument parsing from the URL - trigger it through the ctor

# TODO: Decide the req-res sequence for img_fetch-predict-render_class

class CoverClass(Resource):

    def __init__(self):
        pass

    def post(self, clf_name="vgg16-eurosat"):

        # POSTed 'img' data contains raw satellite image
        src_img = request.json.get('img')
        pred_class = classifier.classify_image(src_img, clf_name)
        
        # TODO: Handle -1 error here?
        return pred_class
        
