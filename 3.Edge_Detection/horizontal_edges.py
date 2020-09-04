from PIL import Image
import numpy as np

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def  vertical_edge_detector(image):
    output=np.zeros_like(image)
    image_padded=np.zeros((image.shape[0]+2,image.shape[1]))
    image_padded[1:-1,:]=image
    image_padded[0,:]=image[0,:]
    image_padded[-1,:]=image[-1,:]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            resultant=image_padded[i+2,j]-image_padded[i,j]
            resultant=round((resultant+255)/2)
            output[i,j]=resultant
    return output

file_name="edge-detection1.png"
im = rgb2gray(np.array(Image.open(file_name)))
pil_img=Image.fromarray(vertical_edge_detector(im)).convert('RGB')
pil_img.save('result_horizontal_edge.jpg')