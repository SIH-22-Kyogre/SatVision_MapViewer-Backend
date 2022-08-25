from flask import jsonify, request
from flask_restful import Resource 

from matplotlib import pyplot as plot

from ..process.fetcher import sentinel


class SatImage(Resource):

    def post(self):

        # bound_box = request.json.get('bbox')
        # img_np = sentinel.fetch_bounds()
        # img_np = sentinel.drive()

        sentinel.check()     

        # plot.imshow(img_np)
        # plot.show()

