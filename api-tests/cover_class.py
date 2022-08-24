import requests
import os
import json
import base64

from PIL import Image
import numpy as np


IMAGES_PATH = os.path.join(
    os.path.abspath(os.path.split(__file__)[0]),
    'assets',
    'images'
)

ENDPOINT = "http://localhost:5000/api/classify/vgg16-eurosat"


# Encode image (Base-64)
with open(os.path.join(IMAGES_PATH, "Residential_1004.jpg"), 'rb') as f:
    img_bytes = f.read()
img_b64 = base64.b64encode(img_bytes).decode("utf8")  

# POST encoded image
payload = json.dumps({
    'img': img_b64
})
headers = {
    'Content-type': 'application/json', 
    'Accept': 'text/plain'
}
response = requests.post(
    ENDPOINT,
    data = payload,
    headers = headers
)
print(response.content)