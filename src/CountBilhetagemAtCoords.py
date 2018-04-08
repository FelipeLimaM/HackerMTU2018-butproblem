def getBusStopsWithFrequency1(data):
	h = {}
	
	for row in data:
		(lat, lon) = (row[10], row[11])
	
		if (lat, lon) not in h:
			h[(lat, lon)] = [1, row]
		else:
			h[(lat, lon)][0] += 1
	
	out = []
	for (lat, lon) in h.keys():
		if h[(lat, lon)] > 8:
			out.append(h[(lat, lon)][1])
	
	return out
	
def getBusStopsWithFrequency(data):
	h = {}
	
	for row in data:
		(lat, lon) = (row[10], row[11])
	
		if (lat, lon) not in h:
			h[(lat, lon)] = 1
		else:
			h[(lat, lon)] += 1
	
	out = []
	for (lat, lon) in h.keys():
		if h[(lat, lon)] > 1:
			out.append((lat, lon, str(h[(lat, lon)])))
	
	return out
