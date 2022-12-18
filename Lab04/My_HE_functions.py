# MyHEFunctions.py

# Import numpy
import numpy as np
# Import plotting functions from matplotlib.
import matplotlib.pyplot as plt

def compute_histogram( image_pixels ):
    # compute_histgram creates a histogram representing the normalized
    # histogram of a normalized image_pixels
    #
    # Syntax:
    #   compute_histogram( image_pixels )
    #
    # Input:
    #   image_pixels = The rows and columns that consist of pixel values
    #
    # Output:
    #   normalized vector of pixel values
    #
    # History:
    #   S. Ruiz-Ramirez     11/04/2022   created

    #gets values row and cols to iterate through matrix
    row, col = image_pixels.shape
    #Vector to store normalized values
    hist = np.zeros(shape=(256))

    #Iterates through image matrix
    for x in range(row):
        for y in range(col):
            #Keeps track of pixel values through vector by tracking each element porportionally
            hist[int(image_pixels[x][y])] += (1/(row * col))
            #Returns Histogram of values
    return hist

    #<your implementation>


def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created

    # Import plotting functions from matplotlib.
    plt.bar( range(256), hist )

    #labels the x-axis
    plt.xlabel('intensity value')

    #Labels the y-axis
    plt.ylabel('PMF') 

    #Displays hist
    plt.show()

def equalize( in_image_pixels ):
    # equalize creates a histogram representing the image with linearized values
    # Matrix of Equalized values
    #
    # Syntax:
    #   equalized( in_image_pixels )
    #
    # Input:
    #   in_image_pixels = The rows and columns that consist of pixel values
    #
    # Output:
    #   Equalized matrix of pixel values
    #
    # History:
    #   S. Ruiz-Ramirez     11/04/2022   created

    #Calculate the normalized image
    normalized = compute_histogram( in_image_pixels )
    #Normal Vector of to keep track of equalized hist
    equalized = np.zeros(shape=(256))
    #Captures the dimensions of the image
    row, col = in_image_pixels.shape
    #Creates Matrix for Equalized Values
    matequalized = np.zeros(shape=(row, col))
    #Tracks the values of the CDF
    total = 0
    
    #Sets the first values normalized value to equalized to track values accordingly
    equalized[0] = normalized[0]
    #Calculates the values for Equalized Histogram
    for beg in range(1, equalized.size):
        #Keeps track of CDF for the equalized value
        total = total + normalized[beg - 1]
        #Equation from 3-15, rounding to get integer value
        equalized[beg] =  ((normalized[beg] + total) * 255).round()

    #Iterates through pizel cols and rows of image
    for x in range(row):
        for y in range(col):
            #Correlates the pixel value to the equivalent equalized values an store in new Matrix
            matequalized[x][y] = equalized[int(in_image_pixels[x][y])]
            #Returns Matrix of equlaization
    return matequalized
