import csv
from datetime import datetime
import sys


def splitDay(data):
	th_manha = (5, 11)
	th_tarde = (th_manha[1]+1, 17)
	th_noite = (th_tarde[1]+1, th_manha[0]-1)

	manha = []
	tarde = []
	noite = []

	for row in data:
		dt = datetime.strptime(row[2].strip(), '%Y-%m-%d %H:%M:%S.000')
		
		if th_manha[0] <= dt.hour <= th_manha[1]: # Manha
			manha.append(row)
		elif th_tarde[0] <= dt.hour <= th_tarde[1]: # Tarde
			tarde.append(row)
		else: # Noite
			noite.append(row)

	return [manha, tarde, noite]
