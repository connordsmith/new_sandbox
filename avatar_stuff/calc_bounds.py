import csv
import random

fi = csv.reader(open('ternary_iso.data'))

lines = list(fi)

i = -1

el_edge_max_MAX = 0
el_edge_max_MIN = 1000
el_edge_mean_MAX = 0
el_edge_mean_MIN = 1000

el_detj_min_MAX = 0
el_detj_min_MIN = 1000
el_detj_max_MAX = 0
el_detj_max_MIN = 1000

for line in lines:
    i += 1
    if (i > 0):
	if (float(line[3]) > el_edge_max_MAX):
	    el_edge_max_MAX = float(line[3])
	if (float(line[3]) < el_edge_max_MIN):
	    el_edge_max_MIN = float(line[3])
	if (float(line[4]) > el_edge_mean_MAX):
	    el_edge_mean_MAX = float(line[4])
	if (float(line[4]) < el_edge_mean_MIN):
	    el_edge_mean_MIN = float(line[4])
	if (float(line[5]) > el_detj_min_MAX):
	    el_detj_min_MAX = float(line[5])
	if (float(line[5]) < el_detj_min_MIN):
	    el_detj_min_MIN = float(line[5])
	if (float(line[6]) > el_detj_max_MAX):
	    el_detj_max_MAX = float(line[6])
	if (float(line[6]) < el_detj_max_MIN):
	    el_detj_max_MIN = float(line[6])


print(str(el_edge_max_MAX) + ',' + str(el_edge_max_MIN) + ',' + str(el_edge_mean_MAX) + ',' + str(el_edge_mean_MIN) + ',' + str(el_detj_min_MAX) + ',' + str(el_detj_min_MIN) + ',' + str(el_detj_max_MAX) + ',' + str(el_detj_max_MIN))



