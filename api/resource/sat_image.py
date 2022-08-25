from flask import jsonify, request
from flask_restful import Resource 

from PIL import Image

from matplotlib import pyplot as plot

from ..process.fetcher import sentinel


class SatImage(Resource):

    def post(self):

        # bound_box = request.json.get('bbox')
        # img_np = sentinel.fetch_bounds()
        img_np = sentinel.drive()
        print(img_np.shape)
        filename = "region.png"
        Image.fromarray(img_np).save(filename)
        print(filename, "saved")
        # sentinel.check()   
        # plot.imshow(img_np)
        # plot.show()

