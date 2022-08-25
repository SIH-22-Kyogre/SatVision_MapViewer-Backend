from email.mime import image
import cv2
import numpy as np
from PIL import Image

def imageOverlay(image1, image2):
    

    image2 //= 50
    
    print(image2)
    print("\n\n\n\n")

    image2[image2==1] = 0 
    image2[image2==2] = 0
    image2[image2==3] = 1
    image2[image2==4] = 1
    image2[image2==5] = 1
    image2[image2==6] = 1
    image2[image2==7] = 1
    image2[image2==8] = 1
    image2[image2==9] = 1

    print(image2)

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    b_channel = image2[:,:,:1]
    # b_channel *= 25
    g_channel = image2[:,:,1:2]
    r_channel = image2[:,:,2:]
    # print(gb_channel.shape)
    image2_recolor = np.stack([
        b_channel.squeeze(),
        g_channel.squeeze(),
        r_channel.squeeze()*255
    ], axis=2)
    print(image2_recolor.shape)
    overlayOutput = cv2.addWeighted(image1, 0.6, image2_recolor, 0.4, 0)
    return overlayOutput

image1 = cv2.imread(r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\custom-0.png")
image2 = cv2.imread(r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\stitched1.png")

image3 = imageOverlay(image1, image2)

print(f"image1 shape: {image1.shape}")
print(f"image2 shape: {image2.shape}")

print(f"image3 type: {type(image3)}")

# Image.fromarray(image3.astype(np.uint8)*25).save("overlay.png")
cv2.imwrite("overlay.png", image3)