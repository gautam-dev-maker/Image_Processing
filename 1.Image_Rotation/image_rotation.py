from PIL import Image
import numpy as np


def rot(image1,turns):
    if turns==0:
        return image1
    else :
        image=np.zeros((image1.shape[1],image1.shape[0],image1.shape[2]))
        for j in range(image1.shape[0]): 
            for i in range(image1.shape[1]): 
                image[i,j,:] = image1[j,i,:]  
        return rot(image[::-1],turns-1)

file_name="rotate.png"
im = np.array(Image.open(file_name))
rotation_angle=int(input("Enter the no. of turns in clockwise direction(by 90 degree) :- "))
im_copy=rot(im,rotation_angle)
pil_img=Image.fromarray((im_copy).astype(np.uint8))
pil_img.save("Rotated.png")
im.rotate(125)