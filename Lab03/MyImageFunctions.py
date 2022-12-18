# we are woring with numpy arrays for implementation
import numpy as np
# Necessary for mathematical functions
from math import floor
from math import ceil
import math

# This function takes as input of a numpy matrix
    # outputs another numpy matrix which is the image resize of the input based on Method (Nearest Neighbor or Bilinear).
    # That is, for each pixel, finds a pixel value of the corresponding location and value
    #
    # Syntax:
    #   out_numpy_matrix = myImageResize(original_matrix, New Row, New Col, interpolation Mathod)
    #
    # Input:
    #   myImageResize(original_matrix, New Row, New Col, interpolation Mathod)
    #
    # Output:
    #   out_numpy_matrix
#Resizes Image on method (Input_Matrix, new row size, new column size, interpolation_method)
def myImageResize(inImage_pixels, M, N, interpolation_method):
    #Gives the size of the input Matrix rows and cosls
    Minput, Ninput = inImage_pixels.shape
    #Creates output matrix with correct sizes
    out = np.zeros(shape=(M, N)) 
    #iterates through array of output matrix for values
    for m in range(0, M+1):  
        for n in range(N+1): 
            #Finds the corresponding row value and column value for each part of the index for a method
            m_inter = (((m-0.5)/M) * Minput) + 0.5  
            n_inter = (((n-0.5)/N) * Ninput) + 0.5
            #Implements Nearest Neighbor in event of
            if interpolation_method == 'nearest':
                #Rounds the value to precise value
                m_inter = round(m_inter)
                n_inter = round(n_inter)
                #inputs the value - 1 in order to maintain bound and stay porportional 
                out[m-1, n-1] = inImage_pixels[m_inter - 1, n_inter - 1]
        
            #Implements Bilinear in event of, implements psuedo code from HW1 Problem 5 Solutions
            elif interpolation_method == 'bilinear':
                if (isinstance(m_inter, int)):
                    m1, m2 = m_inter - 1, m_inter - 1
                else:
                    if(m_inter < 1):
                        m1, m2 = 1, 2
                    elif m_inter > Minput - 1:
                        m1, m2 = Minput - 2, Minput - 1
                    else:
                        m1 = floor(m_inter) -1
                        m2 = ceil(m_inter) -1
                    if (isinstance(n_inter, int)):
                        n1, n2 = n_inter -1, n_inter -1
                    else: 
                        if(n_inter < 1):
                            n1, n2 = 1, 2
                        elif n_inter > Ninput - 1:
                            n1, n2 = Ninput - 2, Ninput - 1
                        else:
                            n1 = floor(n_inter) - 1
                            n2 = ceil(n_inter) - 1
                    p1 = (inImage_pixels[m1][n1])
                    p2 = (inImage_pixels[m1][n2])
                    p3 = (inImage_pixels[m2][n1])
                    p4 = (inImage_pixels[m2][n2])
                    p5 = mybilinear(m1, n1, p1, m1, n2, p2, m2, n1, p3, m2, n2, p4, m_inter - 1, n_inter -1)
                    out[m-1, n-1] = p5
    #Return output Matrix
    return out

# This function takes in points and values from a bilinear method to find p5
    # In order to do p5 compares the values and calculates for the value it should be
    # That is, for each p5 pixel, finds a pixel value of the corresponding location and value
    #
    # Syntax:
    #   p5 = mybilinear(.....)
    #
    # Input:
    #   mybilinear(m1, n1, p1, m1, n2, p2, m2, n1, p3, m2, n2, p4, m_inter - 1, n_inter -1)
    #
    # Output:
    #   p5
#Implements Lecture 7 Notes on Interpolation for perpective points
def mybilinear(x1, y1, p1, x2, y2, p2, x3, y3, p3, x4, y4, p4, x5, y5):
    t1 = (p3 - p1)*((x5 - x1)/(x3 - x1)) + p1
    t2 = (p4 - p2)*((x5 - x2)/(x4 - x2)) + p2
    p5 = (t2 - t1)*((y5 - y1)/(y2 - y1)) + t1
    return p5



# This function takes in arrays to find the RMSE
    # Compares the elements between them
    # returns the difference between Matrixes 
    #
    # Syntax:
    #   RMSE  = myRMSE(original_array, New_array_sized)
    #
    # Input:
    #   myRMSE(original_array, New_array_sized)
    #
    # Output:
    #   RMSE of those arrays
#Implements Lecture 7 Notes on Interpolation for perpective points
def myRMSE(inImage_pixels, new):
    #Finds the difference of the arrays, as well as the square of that. 
    #Finds the mean of those arrays, then roots those values to get RMSE
    MSE = np.square(np.subtract(np.array(inImage_pixels), np.array(new))).mean()
    RMSE = math.sqrt(MSE)
    return RMSE
