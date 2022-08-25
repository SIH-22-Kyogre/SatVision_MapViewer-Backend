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

ENDPOINT = " http://127.0.0.1:5000/api/classify/vgg16-eurosat"


# Encode image (Base-64)

img = Image.open(os.path.join(IMAGES_PATH, "images.png"))
img = img.resize((64, 64))
print(np.asarray(img).shape)
img.save(os.path.join(IMAGES_PATH, "images.png"))

with open(os.path.join(IMAGES_PATH, "images.png"), 'rb') as f:
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