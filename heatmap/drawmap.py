from gmplot import gmplot
import csv

# Place map
gmap = gmplot.GoogleMapPlotter(-23.946528, -46.353571, 13)

# Get bus stops
bus_stops_lat = []
bus_stops_long = []

with open("../data/RMBS_coord_freq_line_904_bus_8611.txt", "rb") as f:
	reader = csv.reader(f)
	
	for row in reader:
		(lat, lon) = (float(row[0]), float(row[1]))
		if lon >= -46.41:
			f = int(row[2])
			
			for i in range(f):
				bus_stops_lat.append(lat)
				bus_stops_long.append(lon)

gmap.heatmap(bus_stops_lat, bus_stops_long, radius = 10, maxIntensity = 40)

# Draw
gmap.draw("my_map.html")
