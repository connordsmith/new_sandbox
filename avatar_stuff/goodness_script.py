import csv
import random

fi = csv.reader(open('isotropic-viz.data'))


#random.shuffle(li)

#fi = open('shuffled.data','w')
#fi.writelines(header)
#fi.writelines(li)
#fi.close()



#r = csv.reader(open('shuffled.data'))
lines = list(fi)

i = -1
#for line in lines:
 #   i += 1
 #   if (i > 0):
#	if (float(line[12]) == -1):
#	    line[15] = 0
 #   	elif (float(line[15]) > .5):
 #   	    line[15] = 1
#	else:
#	    line[15] = 0



for line in lines:
    i += 1
    if (i > 0):
    	if (float(line[12]) > .8):
    	    line[12] = 1
	elif (float(line[12]) > 0):
	    line[12] = 0
	else:
	    line[12] = -1

#drop_tol = line[10]
   


writer = csv.writer(open('three_classes.data','w'))
writer.writerows(lines)
