import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('test_kernel.png')
blur =cv2.GaussianBlur(img,(5,5),1)
pil_img=Image.fromarray(blur)
pil_img.save('gaussian_blur.png')