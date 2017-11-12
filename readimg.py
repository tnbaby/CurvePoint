import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import misc
from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-output', default = '', help = 'output file')

args = parser.parse_args()

lena = mpimg.imread(args.input)
#plt.imshow(lena)
#plt.axis('off') #don't show the axis
#plt.show()

#show the first channel of the picture
##lean_1 = lena[:,:,0]
##plt.imshow(lean_1)
##plt.show()
#show the hot picture
##plt.imshow(lean_1, cmap='Greys_r')
##plt.show()
##
##img = plt.imshow(lean_1)
##img.set_cmap('gray') 
##plt.show()

#convert RGB to gray
#def rgb2gray(rgb):
#	return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
#
#gray = rgb2gray(lena)
#plt.imshow(gray, cmap='Greys_r')
#plt.axis('off')
#plt.show()

#lena_new_sz = misc.imresize(lena, 5.0) # if the second parameter is tuple, that is the output size, while if it is a number, it is the pencentage
#plt.imshow(lena_new_sz)
#plt.show()

I = Image.open(args.input)
I.show()
x = []
y = []
for i in xrange(len(lena)):
	for j in xrange(len(lena[0])):
		rgb = int(lena[i][j][0]) + lena[i][j][1] + lena[i][j][2]
		if rgb < 3 and rgb > 2.9:
			x += [i]
			y += [j]
print len(x), len(y)
plt.plot(y, x, 'b,')
plt.show()
