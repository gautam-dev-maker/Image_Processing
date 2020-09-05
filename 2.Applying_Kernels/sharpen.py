from PIL import Image
import numpy as np
def convolve3d(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.zeros((image.shape[0]+kernel.shape[0]-1,image.shape[1] + kernel.shape[1]-1,image.shape[2]))
    image_padded[kernel.shape[0]-2:-1:,kernel.shape[1]-2:-1:,:] = image
    image_padded[0,0,:]=image[0,0,:]
    image_padded[-1,-1,:]=image[-1,-1,:]
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            for z in range(image.shape[2]):
                summation=(kernel * image_padded[y: y+kernel.shape[0], x: x+kernel.shape[1],z]).sum()
                output[y, x,z]=summation
    output[:,:,3]=image[:,:,3]
    return output



Sharpen=np.array([[-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1],
                  [-1,-1,25,-1,-1],
                  [-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1]])/-25
                  
file_name="test_sharpen.png"
im = np.array(Image.open(file_name))
im=convolve3d(im,Sharpen)
pil_img=Image.fromarray(im.astype(np.uint8))
pil_img.save('result_sharpen.png')



