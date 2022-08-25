from email.mime import image
import cv2
import numpy as np
from PIL import Image

def imageOverlay(image1, image2):
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    overlayOutput = cv2.addWeighted(image1, 0.8, image2, 0.2, 0)
    return overlayOutput

image1 = cv2.imread(r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\custom-0.png")
image2 = cv2.imread(r"D:\\work\\nive\\SSN-College-Of-Engineering\\Extra-Curricular\\UWARL\\sih\\Code\\SatVision_MapViewer-Backend\\stitched1.png")

image3 = imageOverlay(image1, image2)

print(f"image1 shape: {image1.shape}")
print(f"image2 shape: {image2.shape}")

print(f"image3 type: {type(image3)}")

# Image.fromarray(image3.astype(np.uint8)*25).save("overlay.png")
cv2.imwrite("overlay.png", image3)