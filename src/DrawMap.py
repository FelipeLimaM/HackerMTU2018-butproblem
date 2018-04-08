from gmplot import gmplot
import csv

def drawMap(data, solutionCoords):
	# Place map
	gmap = gmplot.GoogleMapPlotter(-23.946528, -46.353571, 13)

	# Get bus stops
	bus_stops_lat = []
	bus_stops_long = []
	scatter_lat = []
	scatter_long = []

	for p in data:
		(lat, lon) = (float(p[0]), float(p[1]))
		if lon >= -46.41: #hardcoded filter
			f = int(p[2])
			
			scatter_lat.append(lat)
			scatter_long.append(lon)
					
			for i in range(f):
				bus_stops_lat.append(lat)
				bus_stops_long.append(lon)

	gmap.heatmap(bus_stops_lat, bus_stops_long, radius = 10, maxIntensity = 40)
	gmap.scatter(scatter_lat, scatter_long, 'cornflowerblue', size=100)
	
	for sol in solutionCoords:
		sol_lat = []
		sol_long = []
		
		for p in sol:
			(lat, lon) = (float(p[0]), float(p[1]))
			sol_lat.append(lat)
			sol_long.append(lon)
		
		sol_lat.append(float(sol[0][0]))
		sol_long.append(float(sol[0][1]))
		
		gmap.plot(sol_lat, sol_long, 'cornflowerblue', edge_width=5)

	# Draw
	gmap.draw("my_map.html")
