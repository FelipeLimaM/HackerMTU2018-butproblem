import csv

def getBilhetagemWithLineAndBus(lines, busses):
	with open("../data/RMBS_bilhetagem_no_botoeiras.txt", "rb") as f:
	reader = csv.reader(f)
	flag = False
	rows = []
	
	for row in reader:
		if flag:
			line = int(row[3])
			bus = int(row[6])
			
		flag = True
	
	return rows
