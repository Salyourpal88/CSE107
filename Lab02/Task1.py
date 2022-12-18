from PIL import Image, ImageOps
from numpy import asarray 
import numpy as np
#Necessary packages^
# open a image from path
im = Image.open('Beginnings.jpg')
# show the image
im.show()

# convert image to gray scale
im_gray = ImageOps.grayscale(im)
#Set the Path of jpg
im_gray_path = 'GrayBeginnings.jpg'
#Save the Image to the jpg
im_gray.save(im_gray_path)
#Open the jpg to save to a VAR 
im2 = Image.open(im_gray_path)
#Display the image
im2.show()

#Save the the array of pixels into a VAR
im_gray_pixels = asarray(Image.open(im_gray_path))
#Display the shape
print("current shape is: ", im_gray_pixels.shape)
max = 0
blade1 = 0
blade2 = 0
#Store the columns and rows from the matrix
rows, cols = im_gray_pixels.shape

#Iterate throught the Matrix 
for row in range(rows):
    for col in range(cols):
        # get the current pixel value
        current_pixel_value = im_gray_pixels[row, col]
        print(col)
        #Keep the Max pixel value of the array, by comparing the previous max
        if current_pixel_value > max:
            max = current_pixel_value
print("maximum pixel value of grayscale image:", max)

#Create a new array that we will store reverse cols and rows to rotate an image
matrix2 = np.empty((cols, rows))
#Get the last to the first column as we go from the first to last each iteration
for y in reversed(range(cols)):
    for x in range(rows):      
        #Store the values while in order of Matrix Size 
        matrix2[blade1][blade2] = im_gray_pixels[x][y]
        blade2 += 1
        if(blade2 == (rows)):
            blade2 = 0
    blade1 +=1

#Create Image from the array
im3 = Image.fromarray(np.uint8(matrix2))
#Store into a jpg
im3.save('counter.jpg')
#Display Image
im3.show()


blade3 = 0
blade4 = 0
#Create a new array that we will store reverse cols and rows to rotate an image
matrix3 = np.empty((cols, rows))
#Iterate through the Image Matrix by the last row to the first, and from first to last column
for y in range(cols):
    for x in reversed(range(rows)):
        #Store the values while in order of Matrix Size
        matrix3[blade3][blade4] = im_gray_pixels[x][y]
        #Keep track of the pixel size
        current_pixel_value = im_gray_pixels[x, y]
        #Compare to ma, if more than max, update max
        if current_pixel_value > max:
            max = current_pixel_value
        blade4 += 1
        if(blade4 == (rows)):
            blade4 = 0
    blade3 +=1


#Store Image version of array into VAR
im4 = Image.fromarray(np.uint8(matrix3))
#Store into jpg
im4.save('clockwise.jpg')
#Display Image
im4.show()
#Display Max pixel value
print("maximum pixel value of clockwise grayscale image:", max)

