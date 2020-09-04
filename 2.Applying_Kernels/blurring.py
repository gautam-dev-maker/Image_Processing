from PIL import Image
import numpy as np

def convolve3d(image, kernel):
    threshold=200
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0]+4,image.shape[1] + 4,image.shape[2]))
    image_padded[3:-1:,3:-1:,:] = image
    image_padded[0,0,:]=image[0,0,:]
    image_padded[-1,-1,:]=image[-1,-1,:]
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            for z in range(image.shape[2]):
                output[y,x,z]=(kernel * image_padded[y: y+5, x: x+5,z]).sum()
    return output

gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256

box_blur=np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])
file_name="test_blur.jpg"
im = np.array(Image.open(file_name))
pil_img=Image.fromarray(convolve3d(im, gaussian_blurr))
pil_img.save('result_blur.jpg')


