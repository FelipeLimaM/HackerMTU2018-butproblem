import csv

with open("../data/RMBS_coord_freq_line_904_bus_8611.txt", "rb") as f:
	reader = csv.reader(f)
	
	for row in reader:
		(lat, lon) = (float(row[0]), float(row[1]))
		if lon >= -46.41:
			f = int(row[2])
			
			if f > 11:
				print(str(lat) + ", " + str(lon) + ", " + str(f))
