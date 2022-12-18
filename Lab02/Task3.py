import numpy as np
from PIL import Image
#Important libraries for program and package^

rows = 100
cols = 256
average = float(0)
#Create a matrix for the Gradient
matrix1 = np.empty((rows, cols))
average2 = 0

#Iterate through the rows and columns 
for x in range(rows):
    for y in range(cols):      
        #Store values 0-254 into the 255 columns of each row
        matrix1[x][y] = y
        #Collect the values of each pixel for a given row
        average = average + y
    if(x == (rows-1)):
        #At the last iteration we calculate the averge by dividing the total amount of pixels
        average = average/(rows*cols)
#Print the Average
print("Here is the average pixel value of the gradient:", average)
#Store Matrix Image into VAR
im4 = Image.fromarray(np.uint8(matrix1))
#Save it into a tif
im4.save('Grayscale.tif')
#Display tif
im4.show()