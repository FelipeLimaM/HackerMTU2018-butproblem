import csv
import re

def getOnlyNumbers(x):
	return re.search("[0-9]+", x).group(0)
	
def getBilhetagemWithLineAndBus(lines, busses):
	with open("../data/RMBS_no_botoeiras2.txt", "rb") as f:
		reader = csv.reader(f)
		flag = False
		rows = []
		
		for row in reader:
			row = [x.strip() for x in row]
			
			if flag:
				line = int(getOnlyNumbers(row[3]))
				bus = int(getOnlyNumbers(row[6]))
				rows.append(row)
				
			flag = True
		
		return rows
