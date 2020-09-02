from PIL import Image
import numpy as np

def convolve3d(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0]+4,image.shape[1] + 4,image.shape[2]))
    image_padded[3:-1:,3:-1:,:] = image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            for z in range(image.shape[2]):
                output[y, x,z]=(kernel * image_padded[y: y+5, x: x+5,z]).sum()
    return output

gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])

box_blur=np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])
Sharpen=np.array([[0 ,-1, 0],
                  [-1, 5,-1],
                  [0 ,-1, 0]])
Edge=np.array([[-1 ,-1, -1],
                  [-1, 8,-1],
                  [-1 ,-1, -1]])
#file_name=input("Enter the name of the image to blurr:- ")
file_name="blur.jpg"
im = np.array(Image.open(file_name))
pil_img=Image.fromarray(convolve3d(im, gaussian_blurr/256))
pil_img.save('gaussian-blurr.jpg')
#print(im)


