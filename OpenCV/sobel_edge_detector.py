import cv2
import numpy as np
from PIL import Image

img = cv2.imread('edge-detection1.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel=np.hypot(sobel_horizontal,sobel_vertical)
pil_img=Image.fromarray(sobel).convert('RGB')
pil_img.save('result_sobel.png')
