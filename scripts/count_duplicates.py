import csv

h  = {}

with open("RMBS_bilhetagem_coord_line_904_bus_8611.txt", "rb") as f:
	reader = csv.reader(f)
	for row in reader:
		(lat, lon) = (row[10], row[11])
		if (lat, lon) not in h:
			h[(lat, lon)] = 1
		else:
			h[(lat, lon)] += 1 

for (lat, lon) in h.keys():
	print(str(lat) + ", " + str(lon) + ", " + str(h[(lat, lon)] * 10000))
