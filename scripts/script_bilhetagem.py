import csv

flag = False

lat1, lon1 = (-23.914870, -46.427610)
lat2, lon2 = (-23.996758, -46.274145)
with open("../dados/stops.txt", "rb") as f:
	reader = csv.reader(f)
	
	for row in reader:
		if flag:
			lat = float(row[4])
			lon = float(row[5])
			
			if lat >= lat2 and lat <= lat1 and lon >= lon1 and lon <= lon2:
				print row
		
		flag = True
