from PIL import Image
import numpy as np
import math

def floating_point(number):
    temp=int(number)
    if number>temp:
        return round(temp+1)
    else :
        return round(temp)

def mat_Multi(angle,x,y,k):
    tangent=math.tan(angle/2)
    if k==0 or k==2:
        X=x-y*tangent
        Y=y
    else:
        X=x
        Y=x*math.sin(angle)+y
    return round(X),round(Y)

def rot(image,angle):
    # Define the most occuring variables
    angle=math.radians(angle)
    cosine=math.cos(angle)
    sine=math.sin(angle)
    
    # Define the height and width of the new image that is to be formed
    new_width = floating_point(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine))
    new_height  = floating_point(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine))

    image1=np.zeros((floating_point(new_width),floating_point(new_height),image.shape[2]))

    # Find the centre of the image about which we have to rotate the image
    centre_row   = round(((image.shape[0]+1)/2)-1)    #with respect to the original image
    centre_column= round(((image.shape[1]+1)/2)-1)    #with respect to the original image

    centre_height= round(((new_height+1)/2)-1)        #with respect to the new image
    centre_width= round(((new_width+1)/2)-1)          #with respect to the new image

    # Now let's traverse through the image matrix
    for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                y=image.shape[0]-1-i-centre_row
                x=image.shape[1]-1-j-centre_column
                X=round(x*cosine+y*sine)
                Y=round(-x*sine+y*cosine)
                X=centre_height-X
                Y=centre_width-Y
               
                if X<image1.shape[1] and Y<image1.shape[0] and X>=0 and Y>=0:
                    image1[Y,X,:]=image[i,j,:]
    for i in range(image1.shape[0]):
        prev = [image1[i][0][0], image1[i][0][1], image1[i][0][2], image1[i][0][3]]
        for j in range(image1.shape[1]-1):
            if (not any(image1[i][j][:])):
                if (any(image1[i][j+1][:])):
                    image1[i][j][:] = prev
            else:
                prev = image1[i][j][:]
    return image1
            

file_name=input("Enter the name of the file:- ")
im = np.array(Image.open(file_name))
rotation_angle=int(input("Enter the no. of turns in clockwise direction(by 90 degree) :- "))
im_copy=rot(im,rotation_angle)
pil_img=Image.fromarray((im_copy).astype(np.uint8))
pil_img.save("rotated_with_bound.png")
