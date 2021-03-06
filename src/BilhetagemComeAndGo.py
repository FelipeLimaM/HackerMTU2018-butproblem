import csv, json
from datetime import datetime


def filterBilhetagemComeAndGo(data):
	list_VT = []
	frequency = {}

	for row in data:
		if row[8] == "V.T.":
			dt = datetime_object = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.000')
			
			if row[1] in frequency:
				if  str(dt.date()) in frequency[row[1]]:
					frequency[row[1]][str(dt.date())]["count"]+=1
					frequency[row[1]][str(dt.date())]["list"].append(row)
				else:
					frequency[row[1]][str(dt.date())]={"count":1,"list":row}
			else:
				frequency[row[1]] = {str(dt.date()) :{"count":1,"list":row}}

	for i in frequency.keys():
		for date in frequency[i].keys():
			if frequency[i][date]["count"] == 2:
				list_VT.append(frequency[i][date]["list"][10])

	return list_VT
