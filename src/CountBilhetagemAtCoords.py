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
		if h[(lat, lon)] > 10:
			out.append((lat, lon, str(h[(lat, lon)])))
	
	return out
