from gmplot import gmplot
import csv

# Place map
gmap = gmplot.GoogleMapPlotter(-23.946528, -46.353571, 13)

# Get bus stops
bus_stops_lat = []
bus_stops_long = []
scatter_lat = []
scatter_long = []

with open("../data/RMBS_coord_freq_line_904_bus_8611.txt", "rb") as f:
	reader = csv.reader(f)
	
	for row in reader:
		(lat, lon) = (float(row[0]), float(row[1]))
		if lon >= -46.41:
			f = int(row[2])
			
			if f > 11:
				scatter_lat.append(lat)
				scatter_long.append(lon)
					
			for i in range(f):
				bus_stops_lat.append(lat)
				bus_stops_long.append(lon)

gmap.heatmap(bus_stops_lat, bus_stops_long, radius = 10, maxIntensity = 40)
gmap.scatter(scatter_lat, scatter_long, 'cornflowerblue', size=100)

# Draw
gmap.draw("my_map.html")
