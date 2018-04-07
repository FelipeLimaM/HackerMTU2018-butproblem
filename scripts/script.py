import csv
import re

def containsOnlyNumbers(x):
	return re.search("[0-9]+", x).group(0)
	 
h  = {}

with open("RMBS_bilhetagem_coord.txt", "rb") as f:
	reader = csv.reader(f)
	for row in reader:
		if int(containsOnlyNumbers(row[3])) == 904 and int(row[6]) == 8611: 
			print(",".join(row))
