import json
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plot
from patchify import patchify, unpatchify
import numpy as np

from .token_manager import *
from .. import classifier

session, token_info = get_oauth_session(gen_token=True)
# print(session)
# print(token_info)

parent_class_map = {
    0: 1,
    1: 1,
    2: 1,
    3: 0,
    4: 0,
    5: 1,
    6: 1,
    7: 0,
    8: 1,
    9: 1
}

def fetch_bounds(
    coord_set,
    bound_box = [
        # 13.822174072265625,
        # 45.85080395917834,
        # 14.55963134765625,
        # 46.29191774991382
        30.705154,
        76.642477,
        30.686567,
        76.677050
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



def classify_stitch_patches(patches, clf_name):

    main_acc = []
    for i in range(patches.shape[0]):

        seg_patches_temp = []
        for j in range(patches.shape[1]):

            patch = patches[i][j]
            class_label = parent_class_map[classifier.classify_image(patch, clf_name)]
            # TODO: Handle model load errors (if label is -1)
            seg_patch = np.full(patch.shape, class_label*255, dtype=int)
            seg_patches_temp.append(seg_patch)

        seg_patches = np.hstack(seg_patches_temp)
        main_acc.append(seg_patches)
        print("Done with", i, "rows")
        
    return np.vstack(main_acc)


# def stitch_patches(patches, orig_shape):
    # print(f"stitch patch shape: {patches.shape}")    
    # image = unpatchify(patches, orig_shape)

    # img_copy = list()
    # for i in range(patches.shape[0]):
    #     for j in range(patches.shape[1]):
    #         img_copy = 

    # return image


def check():

    ND_IMG_PATH = r"D:\\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\images0.png"
    # KD_IMG_PATH = "/home/karthikd/Workspace/Events/SIH'22/repositories/SatVision/Web-Backend/images0.png"

    img = Image.open(ND_IMG_PATH)
    img = np.asarray(img)

    make_patches(img, (64*3, 64*3)), img.shape
    img_restored = classify_stitch_patches(make_patches(img, (64*3, 64*3)), "vgg16-eurosat")

    print(f"img_restored: {img_restored.shape}")
    Image.fromarray(img_restored.astype(np.uint8)).save("CGC-mask-192.png")


def drive():
    coords = {
        "Bengaluru": [77.4255, 12.8752, 77.7176, 13.065],
        "Delhi": [76.5946, 28.366, 77.616, 28.9635],
        "Kolkata": [88.1708, 22.4857, 88.4947, 22.685],
        "Kolkata_fourth": [87.44590370061093, 23.2439811846004, 88.09525564637022, 22.368449655030517],
        "Mumbai": [72.6015, 18.9002, 73.1554, 19.2492],
        "CGC": [
            76.642477, 30.705154, 
            76.677050, 30.686567
        ],
        "Bengaluru_2": [ 
            77.579915, 12.985064,
            77.606919, 12.969623
        ],
        "Delhi_2": [
            77.186769, 28.532386,
            77.196361, 28.527784
        ],
        "India": [
            87.203927, 22.263545,
            77.606919, 12.969623
        ],
        "X": [
            76.6647799, 30.6863144,
            76.6646221, 30.6858911 
        ]
    }

    i = 0
    city = "X"
    val = coords.get(city)
    # print(response.content)
    response = fetch_bounds(val)
    print(response)
    response_img = Image.open(BytesIO(response.content))
    response_img.save(f"{city}_Sat.png")
    return response_img