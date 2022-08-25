import json
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plot
from patchify import patchify
import numpy as np

from .token_manager import *
from .. import classifier

session, token_info = get_oauth_session(gen_token=True)
# print(session)
# print(token_info)


def fetch_bounds(
    coord_set,
    bound_box = [
        13.822174072265625,
        45.85080395917834,
        14.55963134765625,
        46.29191774991382
    ],
    bands = ["B02", "B03", "B04"],
    dimensions = (512, 512)
    # TODO: Add dimsensions to the post specifications

):
    response = session.post(
        'https://services.sentinel-hub.com/api/v1/process',
        headers = {
            "Content-Type": "application/json"
        },
        data = json.dumps({
            "input": {
                "bounds": {
                    "bbox": coord_set
                },
                "data": [{
                    "type": "sentinel-2-l2a"
                }]
            },
            "output": {
                "width": 2496,
                "height": 2496
            },
            "evalscript": """

            function setup() {
            return {
                input: ["B02", "B03", "B04"],
                output: {
                bands: 3
                }
            };
            }

            function evaluatePixel(
            sample,
            scenes,
            inputMetadata,
            customData,
            outputMetadata
            ) {
            return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
            }
            """
        })
    )
    return response


def make_patches(img, patch_shape):

    # channels = np.moveaxis(img, -1, 0)
    # patches = []
    # for channel in channels:
    #     chnl_patches = patchify(channel, patch_shape, step=patch_shape[0])
    #     patches.append(patchify(channel, patch_shape, step=channel.shape[0]))
    
    return patchify(img, (*patch_shape, 3), patch_shape[0]).squeeze()


def classify_patches(patches, clf_name):

    seg_patches = []
    for i in range(patches.shape[0]):
        seg_patches_temp = []
        for j in range(patches.shape[1]):
            patch = patches[i][j]
            class_label = classifier.classify_image(patch, clf_name)
            # TODO: Handle model load errors (if label is -1)
            seg_patch = np.full(patch.shape, class_label, dtype=int)
            seg_patches_temp.append(seg_patch)
        seg_patches.append(seg_patches)
        print(i)
    return np.array(seg_patches).shape


def stitch_patches(patches, orig_shape):    
    image = unpatchify(patches, orig_shape)
    return image


def check():
    img = Image.open("/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/images0.png")
    img = np.asarray(img)
    
    img_restored = stitch_patches(classify_patches(make_patches(img, (64, 64)), "vgg16-eurosat"), img.shape)
    Image.fromarray(img_restored).save("stitched1.png")


def drive():
    coords = {
        "Bengaluru": [77.4255, 12.8752, 77.7176, 13.065],
        "Delhi": [76.5946, 28.366, 77.616, 28.9635],
        "Kolkata": [88.1708, 22.4857, 88.4947, 22.685],
        "Mumbai": [72.6015, 18.9002, 73.1554, 19.2492],
    }

    i = 0
    val = coords.get("Kolkata")
    # print(response.content)
    response = fetch_bounds(val)
    response_img = Image.open(BytesIO(response.content))
    response_img.save(f"images{i}.png")
    return response_img