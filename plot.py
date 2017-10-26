import numpy
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-output', default = '', help = 'output file')

args = parser.parse_args()

x = []
y = []
for count, line in enumerate(open(args.input)):
	i, j = line.split(',')
	x += [float(i.strip())]
	y += [float(j.strip())]
step = (max(x) - min(x))/len(x)
margin = 100*step

#plt.plot(x, y, 'b+')
#plt.show()
singular_xpoints = []
singular_ypoints = []
neighbors_index = {}
neighbor_cnts = {}
list.sort(x)
flag = False
for i in xrange(len(x)):
	for j in xrange(len(x)):
		if(abs(x[j] - x[i]) > margin):
			continue
		key = str(x[i])+'@'+str(y[i])
		if neighbor_cnts.has_key(key):
			neighbor_cnts[key] += 1
		else:
		 	neighbor_cnts[key] = 1
		if neighbors_index.has_key(key):
			neighbors_index[key] += [j] 
		else:
		 	neighbors_index[key] = [j]
		flag = True
		if i < len(x)/2 and y[j] < y[i]:
			break
		if i >= len(x)/2  and y[j] > y[i]:
			break
	else:
	  	if flag:
	 		singular_xpoints += [x[i]]
	 		singular_ypoints += [y[i]]
print margin
plt.plot(x, y, 'k,')
plt.plot(singular_xpoints, singular_ypoints, 'r+')
plt.show()
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
