import csv

def DateToInt(date):
	date = date.split()
	hms = date[1]
	hms = hms.replace("'", "")
	hms = hms.split(":")
	
	return 3600 * int(hms[0]) + 60 * int(hms[1]) + int(hms[2])
	
def searchBestHourFit(A, h):
	best_index = 0
	best_value = 999999999
	
	for i in range(len(A)):
		if abs(A[i][0] - h) < best_value:
			best_value = abs(A[i][0] - h)
			best_index = i
	
	return (A[best_index][1], A[best_index][2], A[best_index][3])

data  = []

with open("../HackerMTU2018-butproblem/data/linha_904_cgs_2016_01/transmissoes_86110001.csv", "rb") as f:
	reader = csv.reader(f)
	flag = False
	
	for row in reader:
		if flag:
			date = row[59] #timestampModulo
			data.append((DateToInt(date), float(row[33]), float(row[35]), date))
		
		flag = True

with open("../HackerMTU2018-butproblem/tmp/bus8611.csv", "rb") as f:
	reader = csv.reader(f)
	flag = False
	
	for row in reader:
		if flag:
			date = row[2] #timestampModulo
			hour = DateToInt(date)
			
			aux = searchBestHourFit(data, hour)
			print(str(aux[0]) + " , " + str(aux[1]))
		
		flag = True
