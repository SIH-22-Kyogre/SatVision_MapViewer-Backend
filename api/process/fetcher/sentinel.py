import json
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plot

from .token_manager import *

session, token_info = get_oauth_session(gen_token=True)
# print(session)
# print(token_info)


def fetch_bounds(
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
                    "bbox": bound_box
                },
                "data": [{
                    "type": "sentinel-2-l2a"
                }]
            },
            "output": {
                "responses": [{
                    "identifier": "default",
                    "format": {
                        "type": "image/png"
                    }
                }]
            },
            "evalscript": """

            function setup() {
                return {
                input: {bounds},
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
            """.format(bounds=str(bounds))
        })
    )

    # print(response.content)
    response_img = Image.open(BytesIO(response.content))
    # plot.imshow(response_img)
    # plot.show()
    return response_img