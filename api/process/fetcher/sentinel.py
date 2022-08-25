import json
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plot

from .token_manager import *

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
    "evalscript": """
    //VERSION=3

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

def drive():
    coords = {
        "Bengaluru": [77.4255, 12.8752, 77.7176, 13.065],
        "Delhi": [76.5946, 28.366, 77.616, 28.9635],
        "Kolkata": [88.1708, 22.4857, 88.4947, 22.685],
        "Mumbai": [72.6015, 18.9002, 73.1554, 19.2492],
    }

    for i, val in enumerate(coords.values()):
        # print(response.content)
        response = fetch_bounds(val)
        response_img = Image.open(BytesIO(response.content))
        response_img.save(f"images{i}.png")
    return response_img