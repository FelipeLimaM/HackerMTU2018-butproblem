import csv
import bisect

def DateToInt(date):
	date = date.split()
	hms = date[1]
	hms = hms.replace(".000", "")
	hms = hms.split(":")
	
	return 3600 * int(hms[0]) + 60 * int(hms[1]) + int(hms[2])
	
def searchBestHourFit(A, h):
	best_index = 0
	best_value = 999999999
	
	for i in range(len(A)):
		if abs(A[i][0] - h) < best_value:
			best_value = abs(A[i][0] - h)
			best_index = i
	
	return (A[best_index][1], A[best_index][2])

'''
@gomesar Nao testei
'''
def searchBestHourFit(A, h):
	aux = bisect.bisect(A, h)
        return A[aux][1], A[aux][2]
	
def getBilhetagemWithCoords(data, lines, busses):
	timesCoords = []
	
	#first read the gps data to get pairs of (time, coords)
	for i in range(len(lines)):
		with open("../data/linha_" + str(lines[i]) + "_cgs_2016_01/transmissoes_" + str(busses[i]) + "0001.csv", "rb") as f:
			reader = csv.reader(f)
			flag = False
			
			for row in reader:
				if flag:
					date = row[59] #timestampModulo
					timesCoords.append((DateToInt(date), float(row[33]), float(row[35])))
				
				flag = True
	
        #sort
        timesCoords.sort(key=lambda x: x[0]) # @gomesar para busca binaria
	#for each row, find the closest time and append the coords
	for row in data:
		date = row[2] #timestampModulo
		hour = DateToInt(date)
		aux = searchBestHourFit(timesCoords, hour)
		row.append(str(aux[0]))
		row.append(str(aux[1]))
	
	return data
