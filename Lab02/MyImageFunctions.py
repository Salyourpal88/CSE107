import numpy as np 
from PIL import Image
#Import numpy and pillow

def myImageInverse(inImage):
#This function get a matrix
#Creates a new array with the same rows and columns
#Stores the inverse by getting the pixel value 
#Then subtracts that to 255
#This function also keeps track of the new arrays highest pixel value
#Prints it out for the Max pixel value of the inverse image
#Stores the image matrix into a VAR
#Saves that to a new tif
#Displays the inverse Image Image
#Returns the output matrix of the inverse
#
#Syntax: output = def myImageInverse(data)
#
#Input: inImage = matrix pixel values of Watertower.tif
#
#Output:output = 255 - inImage for weach pixel value
#
#History: 
# S. Ruiz-Ramirez 9/21/22 Created
# S. Ruiz-Ramirez 9/21/22 Made the new matrix
# S. Ruiz-Ramirez 9/21/22 Stored proper values
# S. Ruiz-Ramirez 9/21/22 Kept track of max value
# S. Ruiz-Ramirez 9/21/22 Created, Stored, and displayed image
# S. Ruiz-Ramirez 9/21/22 Returned the output matrix
    rows, cols = inImage.shape
    output = np.empty((rows, cols))
    max = 0

    for x in range(rows): #0 1 3.....99
        for y in range(cols): #0-254 [0] #0-254 [1]     
            output[x][y] = 255 - inImage[x][y]
            current_pixel_value = output[x][y]
            if current_pixel_value > max:
                max = current_pixel_value
    print("Here's the max:", max)
    im3 = Image.fromarray(np.uint8(output))
    im3.save('Watertower_my.tif')
    im3.show()
    return output

