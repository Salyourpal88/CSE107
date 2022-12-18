from PIL import Image
from numpy import asarray
from MyImageFunctions import *
#Important libraries for program and package^

output = np.empty((332, 218))
# open a image from path
im = Image.open('Watertower.tif')
# show the image
im.show()
#Store Image as matrix
data = asarray(im)
#Call function from MyImageFunctions
output = myImageInverse(data)
print(output)
