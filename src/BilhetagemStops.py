import csv
from math import sqrt

def getClosestBusStop(data):
	with open('../data/RMBS_stops.txt', 'rb') as stops:
		stopsreader = list(csv.reader(stops, delimiter=',', quotechar='\n'))
		for cardsreader in data:
			for i in cardsreader:
				distance_i = sqrt( (float(stopsreader[0][2]) - float(i[10]))**2 + (float(stopsreader[0][3]) - float(i[11]))**2 )
				line = stopsreader[0]
				for j in stopsreader:
					distance_here = sqrt( (float(j[2]) - float(i[10]))**2 + (float(j[3]) - float(i[11]))**2 )
					if distance_here < distance_i:
						distance_i = distance_here
						line = j

				i[10] = line[2]
				i[11] = line[3]
				writer.writerow(i)
	
	return data
