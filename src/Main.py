import csv
from LineAndBusBilhetagem import getBilhetagemWithLineAndBus
from BilhetagemCoords import getBilhetagemWithCoords
from CountBilhetagemAtCoords import getBusStopsWithFrequency
from ConvertToCVRP import createCVRPInput
from DrawMap import drawMap

lines = []
busses = []

with open("in/test.txt", "rb") as f:
	reader = csv.reader(f)
	flag = False
	
	for row in reader:
		if flag:
			lines.append(int(row[0]))
			busses.append(int(row[1]))
		
		flag = True

data = getBilhetagemWithLineAndBus(lines, busses)

#filtro de horario entra aqui

data = getBilhetagemWithCoords(data, lines, busses)

#filtro para encontrar ponto mais proximo entra aqui

data = getBusStopsWithFrequency(data)

filename = createCVRPInput(data, len(lines))

#roda o algoritmo do CVRP

solutionCoords = getCoordsFromCVRPSol(filename)

drawMap(data, solutionCoords)
