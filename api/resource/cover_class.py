from flask import request
from flask_restful import Resource 

# NOTE: Use reqparse instances for argument parsing from the URL - trigger it through the ctor

# TODO: Decide the req-res sequence for img_fetch-predict-render_class

class CoverClass(Resource):

    def __init__(self):
        pass

    def post(self):
        # POSTed 'img' data contains raw satellite image
        src_img = request.form['img']
        
