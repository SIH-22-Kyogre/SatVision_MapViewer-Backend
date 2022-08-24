import requests
import os
from PIL import Image
import numpy as np

IMAGES_PATH = os.path.join(
    os.path.abspath(os.path.split(__file__)[0]),
    'assets',
    'images'
)


endpoint = "localhost:5000/api/classify"

response = requests.post(
    endpoint, 
    json = {
        'img': np.asarray(
            Image.open(os.path.join(
                IMAGES_PATH,
                "Residential_1004.jpg"
            ))
        )
    }
)

print(response.content)