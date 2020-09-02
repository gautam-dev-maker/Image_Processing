from PIL import Image
import numpy as np

def convolve3d(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0]+2,image.shape[1] + 2,image.shape[2]))
    image_padded[1:-1:,1:-1:,:] = image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            for z in range(image.shape[2]):
                output[y, x,z]=(kernel * image_padded[y: y+3, x: x+3,z]).sum()
    return output


Sharpen=np.array([[0 ,-1, 0],
                  [-1, 5,-1],
                  [0 ,-1, 0]])
Edge=np.array([[-1 ,-1, -1],
                  [-1, 8,-1],
                  [-1 ,-1, -1]])
#file_name=input("Enter the name of the image to blurr:- ")
file_name="sharpening.png"
im = np.array(Image.open(file_name))
pil_img=Image.fromarray(convolve3d(im, Sharpen))
pil_img.save('sharpened.png')
print(im.shape)
#print(im)


