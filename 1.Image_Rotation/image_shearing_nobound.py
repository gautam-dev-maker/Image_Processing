from PIL import Image
import numpy as np
import math

def floating_point(number):
    temp=int(number)
    if number>temp:
        return temp+1
    else :
        return number

def mat_Multi(angle,x,y,k):
    tangent=math.tan(angle/2)
    if k==2 or k==0:
        X=x-y*tangent
        Y=y
    if  k==1:
        X=x
        Y=x*math.sin(angle)+y
    return round(X),round(Y)

def rot(image,angle):

    # Define the most occuring variables
    angle=math.radians(angle)
    cosine=math.cos(angle)
    sine=math.sin(angle)
    image1=np.zeros_like(image)
    image2=np.zeros_like(image)

    # Find the centre of the image about which we have to rotate the image
    centre_row   = round(((image.shape[0]+1)/2)-1)
    centre_column= round(((image.shape[1]+1)/2)-1)
    for k in range(3):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                y=image.shape[0]-1-i-centre_row
                x=image.shape[1]-1-j-centre_column
                #X,Y=mat_Multi(angle,x,y,k)
                if k==0:
                    X,Y=mat_Multi(angle,x,y,0)
                elif k==1:
                    X,Y=mat_Multi(angle,x,y,0)
                    X,Y=mat_Multi(angle,X,Y,1)
                elif k==2:
                    X,Y=mat_Multi(angle,x,y,0)
                    X,Y=mat_Multi(angle,X,Y,1)
                    X,Y=mat_Multi(angle,X,Y,2)
                X=centre_column-X
                Y=centre_row-Y
                if X<image1.shape[1] and Y<image1.shape[0] and X>=0 and Y>=0:
                    if k==2:
                        image2[Y,X,:]=image[i,j,:]
                    else:
                        image1[Y,X,:]=image[i,j,:]
    return image2
            

            


file_name="rotate.png"#input("Enter the name of the file:- ")
im = np.array(Image.open(file_name))
rotation_angle=-int(input("Enter the no. of turns in clockwise direction(by 90 degree) :- "))
im_copy=rot(im,rotation_angle)
pil_img=Image.fromarray((im_copy).astype(np.uint8))
pil_img.save("rotated_sheared_without_bound.png")
