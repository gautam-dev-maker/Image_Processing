from PIL import Image
import numpy as np
def convolve3d(image, kernel):
    threshold=100
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0]+2,image.shape[1] + 2,image.shape[2]))
    image_padded[1:-1:,1:-1:,:] = image
    image_padded[0,0,:]=image[0,0,:]
    image_padded[-1,-1,:]=image[-1,-1,:]
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            for z in range(image.shape[2]):
                summation=(kernel * image_padded[y: y+3, x: x+3,z]).sum()
                if summation<threshold :
                    output[y, x,z]=50
                else:
                    output[y, x,z]=summation
    output[:,:,3]=image[:,:,3]
    return output


Sharpen=np.array([[-1,-1, -1],
                  [-1, 9,-1],
                  [-1 ,-1, -1]])
# Edge=np.array([   [0 ,-1, 0],
#                   [-1, 4,-1],
#                   [0 ,-1, 0]])
                  
file_name="test_sharpen.png"
im = np.array(Image.open(file_name))
pil_img=Image.fromarray(convolve3d(im,Sharpen*0.9))
pil_img.save('result_sharpen.png')



