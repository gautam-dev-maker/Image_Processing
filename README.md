## Image Processing Task

The following operations have been performed mainly using only Numpy and Pillow library is used just to load and save image.

### 1. Image Rotation

The image can be rotated by any angle bound or inbound.It involves finding the centre of the Matrix and Shifting along the centre using Rotation Matrix

![Rotation Matrix](https://legacy.voteview.com/images/homework_1_1_18_2011.jpg)

|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotate.png">| 
|:---:|
|Input Image|


**Output**
|<img width="600" height="322" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotated_without_bound.png">|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotated_with_bound.png">|
|:---:|:---:|
|No Bound|Bound|

### 2. Applying Kernels

Convolution is a simple mathematical operation which is fundamental to many common image processing operators. Convolution provides a way of multiplying together two arrays of numbers, generally of different sizes, but of the same dimensionality, to produce a third array of numbers of the same dimensionality.Kernels form the Second Matrix which provides effects to the Image.
![figure3](https://user-images.githubusercontent.com/35737777/68632479-95c61f80-04e6-11ea-80b2-2e86a4fcc258.jpg)

Applying 5X5 filters to do the following task
1. Blurring 
2. Sharpening

|<img width="446" height="447" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/2.Applying_Kernels/test_sharpen.png">|
|:---:|
|Input Image|

**Output**
|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/2.Applying_Kernels/result_box_blur.png">|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/2.Applying_Kernels/result_blur.png">|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/2.Applying_Kernels/result_sharpen.png">|
|:---:|:---:|:---:|
|Box Blur|Gaussian Blur|Sharpen|

### 3. Edge Detection

Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness.

Applying Edge Detection in following sequence 
1. Vertical edge detection
2. Horizontal edge detection
3. Sobel edge detection (right, left, top, bottom)
4. Canny edge detection  

|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/edge-detection1.png">|
|:---:|
|Input Image|

**Output**
|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/result_verical_edge.jpg">|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/result_horizontal_edge.jpg">|
|:---:|:---:|
|Vertical Edge Detection|Horizontal Edge Detection|
|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/result_sobel.jpg">|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/result_canny.jpg">|
|Sobel Edge Detection|Canny Edge Detection|

### 4. Morphological Transformation
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation.
Applying dilation and erosion transformation to the image

**Output**
|<img width="112" height="150" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/4.Morphological_Transformation/morphological.png">|<img width="112" height="150" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/4.Morphological_Transformation/result_dilation.png">|<img width="112" height="150" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/4.Morphological_Transformation/result_erosion.png">|<img width="112" height="150" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/4.Morphological_Transformation/dilation-edge_detection.jpg">|
|:---:|:---:|:---:|:---:|
|Input-Image|Dilation|Erosion|Edge-Detection|

