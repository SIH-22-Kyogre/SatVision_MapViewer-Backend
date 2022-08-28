from flask import jsonify, request
from flask_restful import Resource 

from PIL import Image

from matplotlib import pyplot as plot

from ..process.fetcher import sentinel

import cv2
import numpy as np

def imageOverlay(image1, image2):
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    overlayOutput = cv2.addWeighted(image1, 0.6, image2, 0.4, 0)
    return overlayOutput

class SatImage(Resource):

    def post(self):

        # bound_box = request.json.get('bbox')
        # img_np = sentinel.fetch_bounds()
        img_np = sentinel.drive()
        sentinel.check()   
        # plot.imshow(img_np)
        # plot.show()

        image1 = cv2.imread(r"/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/Gujarat_Sat.png")
        image2 = cv2.imread(r"/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/CGC-mask-192.png")

        image3 = imageOverlay(image1, image2)

        print(f"image1 shape: {image1.shape}")
        print(f"image2 shape: {image2.shape}")

        print(f"image3 type: {type(image3)}")

        # Image.fromarray(image3.astype(np.uint8)*25).save("overlay.png") - DON'T DO THIS - MATCH!
        cv2.imwrite("CGC-overlay-res152.png", image3)

        



