def getCoordsFromCVRPSol(filename):
	h = {}

	#cria uma hash de id -> coords
	i = 0
	with open("/tmp/" + filename + ".vrp", "rb") as f:
		for row in f:
			i += 1
			if i >= 8:
				if row == "DEMAND_SECTION\n":
					break
					
				row = row.split()
				h[int(row[0])] = (row[1], row[2])

	#retorna listas de coords para cada rota
	coords = []
	with open("../tmp/" + filename + ".out", "rb") as f:
		for row in f:
			aux = []
			row = row.split()
			
			for v in row:
				v = int(v)
				aux.append((h[v + 1][0],h[v + 1][1]))
			
			coords.append(aux)
	
	return coords
