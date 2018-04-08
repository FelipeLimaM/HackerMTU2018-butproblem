import csv
from LineAndBusBilhetagem import getBilhetagemWithLineAndBus
from BilhetagemCoords import getBilhetagemWithCoords
from CountBilhetagemAtCoords import getBusStopsWithFrequency
from ConvertToCVRP import createCVRPInput
from DrawMap import drawMap
from BilhetagemStops import getClosestBusStop
from ConvertCVRPSolToCoords import getCoordsFromCVRPSol

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

print("Removendo linhas e onibus nao interessados")
data = getBilhetagemWithLineAndBus(lines, busses)

#filtro de horario entra aqui

print("Fazendo o match de bilhetagem com os dados do GPS")
data = getBilhetagemWithCoords(data, lines, busses)

print("Encontrando o pto de onibus mais proximo")
data = getClosestBusStop(data)

print("Calculando a frequencia de cada pto de onibus")
data = getBusStopsWithFrequency(data)

print("Criando o input para o CVRP")
filename = createCVRPInput(data, len(lines))

print("Rodando o algoritmo do CVRP")
#roda o algoritmo do CVRP

print("Transferindo a solucao de ID para coordenadas")
solutionCoords = getCoordsFromCVRPSol(filename)

print("Desenhando no mapa a solucao")
drawMap(data, solutionCoords)
