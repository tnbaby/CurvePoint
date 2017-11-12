import numpy
import matplotlib.pyplot as plt
import argparse
import matplotlib.image as mpimg

parser = argparse.ArgumentParser()

parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-output', default = '', help = 'output file')

args = parser.parse_args()

x = []
y = []
#test_hash = {}
lena = mpimg.imread(args.input)
#plt.imshow(lena)
#plt.show()
for i in xrange(len(lena)):
	for j in xrange(len(lena[0])):
		rgb = int(lena[i][j][0]) + lena[i][j][1] + lena[i][j][2]
		if rgb == 0:
#		 if test_hash.has_key(str(i)+'@'+str(j)):
#				continue
#			test_hash[str(i)+'@'+str(j)] = 1	
			y += [i]
			x += [j]

    
y_mean = numpy.mean(y)
for i in xrange(len(y)):
	if y[i] > y_mean:
		y[i] = y_mean - (y[i] - y_mean)
	else:
		y[i] = y_mean + (y_mean - y[i])
	
x0 = int(numpy.mean(x))
y0 = int(numpy.mean(y))
x_collection = []
y_collection = []
next_point = True
current_x = x0
current_y = y0
direction = 0
flag = 1
cnt = 0
for i in xrange(len(x)):
	if x[i] - x0 < 15 and x[i] - x0 > 0 and y[i] - y0 > 0 and y[i] - y0 < 40:
		x0 = x[i]
		y0 = y[i]
		print x0, y0
		break
plt.plot(x, y, 'k,')
plt.plot(x0, y0, 'r+')
plt.show()
cell_length = 40
while next_point:
	cnt += 1
	next_point = False
	if int(lena[current_x + cell_length][current_y + cell_length][0]) + lena[current_x + cell_length][current_y + cell_length][1] + lena[current_x + cell_length][current_y + cell_length][2] == 0:
		next_point = True
		direction += 1
	if int(lena[current_x + 10][current_y - cell_length][0]) + lena[current_x + cell_length][current_y - cell_length][1] + lena[current_x + cell_length][current_y - cell_length][2] == 0:
		next_point = True
		direction -= 1
	if int(lena[current_x - cell_length][current_y + cell_length][0]) + lena[current_x - cell_length][current_y + cell_length][1] + lena[current_x - cell_length][current_y + cell_length][2] == 0:
		next_point = True
		direction -= 1
	if int(lena[current_x - cell_length][current_y - cell_length][0]) + lena[current_x - cell_length][current_y - cell_length][1] + lena[current_x - cell_length][current_y - cell_length][2] == 0:
		next_point = True
		direction += 1
	if direction > 0:
		# up right direction
		if flag  == 1:
			# up
			x_collection += [current_x + cell_length]
			y_collection += [current_y + cell_length]
			current_x += cell_length
			current_y += cell_length
		else:
			# down
			x_collection += [curretn_x - cell_length]
			y_collection += [current_y - cell_length]
			current_x += cell_length
			current_y -= cell_length
		direction = 0
	else: 
		# have to change direction
		if flag == 1:
			flag = -1
			x_collection += [current_x - cell_length]
			y_collection += [current_y - cell_length]
			current_x -= cell_length
			current_y -= cell_length
		else:
			flag = 1
			x_collection += [current_x + cell_length]
			y_collection += [current_x + cell_length]
			current_x += cell_length
			current_y += cell_length
	lena[current_x][current_y][0] = bytes(90)
	lena[current_x][current_y][1] = bytes(90)
	lena[current_x][current_y][2] = bytes(90)
	if cnt % 100 == 0:
		plt.imshow(lena)
		plt.show()
	print next_point	
#plt.imshow(lena)
#plt.show()
#for count, line in enumerate(open(args.input)):
#	i, j = line.split(',')
#	x += [float(i.strip())]
#	y += [float(j.strip())]

#margin = (max(x) - min(x))/10
#print len(x)
#x_mean = numpy.mean(x)
#for i in xrange(len(x)):
#	if x[i] > x_mean:
#		x[i] = x_mean - (x[i] - x_mean)
#	else:
#		x[i] = x_mean + (x_mean - x[i])
#plt.plot(y, x, 'b,')
#plt.show()
#print margin, max(y) - min(y), max(x) - min(x)
#
#flag_matrix = [[0 for i in xrange(int((max(y) - min(y))/margin)+1)] for j in xrange(int((max(x) - min(x))/margin)+1)]
#

######################################################
# collecting the points of curve
######################################################

######################################################
#	sample some points to reduce some cluster
######################################################
##sample_x = []
##sample_y = []
##for i in xrange(len(x)):
##	x_index = int((x[i] - min(x)) / margin)
##	y_index = int((y[i] - min(y)) / margin)
##
##	if len(sample_x) == 0:
##		sample_x += [x[i]]
##		sample_y += [y[i]]
##	elif flag_matrix[x_index][y_index] == 0:
##	 	sample_x += [x[i]]
##	 	sample_y += [y[i]]
##		flag_matrix[x_index][y_index] = 1
##	#print i
###print i, len(sample_x)
##plt.plot(sample_y, sample_x, 'r.')
##plt.show()
##
########################################################
# a way to lable dense points
########################################################
##singular_xpoints = []
##singular_ypoints = []
##neighbors_index = {}
##neighbor_cnts = {}
##list.sort(x)
##flag = False
##for i in xrange(len(x)):
##	for j in xrange(len(x)):
##		if(abs(x[j] - x[i]) > margin):
##			continue
##		key = str(x[i])+'@'+str(y[i])
##		if neighbor_cnts.has_key(key):
##			neighbor_cnts[key] += 1
##		else:
##		 	neighbor_cnts[key] = 1
##		if neighbors_index.has_key(key):
##			neighbors_index[key] += [j] 
##		else:
##		 	neighbors_index[key] = [j]
##		flag = True
##		if i < len(x)/2 and y[j] < y[i]:
##			break
##		if i >= len(x)/2  and y[j] > y[i]:
##			break
##	else:
##	  	if flag:
##	 		singular_xpoints += [x[i]]
##	 		singular_ypoints += [y[i]]
##print margin
##plt.plot(x, y, 'k,')
##plt.plot(singular_xpoints, singular_ypoints, 'r+')
##plt.show()
#
#line_x = []
#line_y = []
#index = [0]
#
#while len(index) > 0:
#	key = str(x[index[0]])+'@'+str(y[index[0]])
#	cnt = None
#	ind = None
#	index = []
#	for neighbor in neighbors_index[key]:
#		if cnt < neighbor_cnts[str(x[neighbor])+'@'+str(y[neighbor])]:
#			cnt = neighbor_cnts[str(x[neighbor])+'@'+str(y[neighbor])]
#			ind = neighbor
#	if ind != None:
#		line_x += [x[ind]]
#		line_y += [y[ind]]
#		index = [ind]
#plt.plot(line_x, line_y, 'b+')
#plt.show()
##plt.savefig(args.output, dpi = 500)
