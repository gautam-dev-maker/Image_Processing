import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread("edge-detection1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 602, 452)

titles = ['image', 'canny']
images = [img, canny]
pil_img=Image.fromarray(canny).convert('RGB')
pil_img.save('result_canny.png')
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()