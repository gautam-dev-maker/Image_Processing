from PIL import Image
import numpy as np
import math


# def rot_perfect_angles(image1,turns):
#     if turns==0:
#         return image1
#     else :
#         image=np.zeros((image1.shape[1],image1.shape[0],image1.shape[2]))
#         for j in range(image1.shape[0]): 
#             for i in range(image1.shape[1]): 
#                 image[i,j,:] = image1[j,i,:]  
#         return rot(image[::-1],turns-1)


def floating_point(number):
    temp=int(number)
    if number>temp:
        return temp+1
    else :
        return number

# def mat_Multi(angle,x,y,k):
#     tangent=math.tan(angle/2)
#     if k==0 or k==2:
#         X=x-y*tangent
#         Y=y
#     else:
#         X=x
#         Y=x*math.sin(angle)+y
#     return round(X),round(Y)

def rot(image,angle):
    # Define the most occuring variables
    angle=math.radians(angle)
    cosine=math.cos(angle)
    sine=math.sin(angle)
    
    #image1=np.zeros_like(image)

    # Define the height and width of the new image that is to be formed
    new_height = floating_point(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine))
    new_width  = floating_point(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine))

    image1=np.zeros((new_width,new_height,image.shape[2]))

    # Find the centre of the image about which we have to rotate the image
    centre_row   = round(((image.shape[0]+1)/2)-1)
    centre_column= round(((image.shape[1]+1)/2)-1)

    # centre_height= round(((new_height+1)/2)-1)
    # centre_width= round(((new_width+1)/2)-1)

    # Now let's traverse through the image matrix
    for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                y=image.shape[0]-1-i-centre_row
                x=image.shape[1]-1-j-centre_column
                X=round(x*cosine+y*sine)
                Y=round(-x*sine+y*cosine)
                X=centre_column-X
                Y=centre_row-Y
                if X<image1.shape[1] and Y<image1.shape[0] and X>=0 and Y>=0:
                    image1[Y,X,:]=image[i,j,:]
    return image1
            

            


file_name="rotate.png"
im = np.array(Image.open(file_name))
#rotation_angle=int(input("Enter the no. of turns in clockwise direction(by 90 degree) :- "))
im_copy=rot(im,80)
pil_img=Image.fromarray((im_copy).astype(np.uint8))
pil_img.save("Rotated.png")

