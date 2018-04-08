import csv
from datetime import datetime
import sys


def splitDay(csv_file, verbose=True):
    th_manha = (5, 11)
    th_tarde = (th_manha[1]+1, 17)
    th_noite = (th_tarde[1]+1, th_manha[0]-1)

    if verbose:
        print("Divisao de turnos:")
        print("Manhã: {} - {}".format(th_manha[0], th_manha[1]))
        print("Tarde: {} - {}".format(th_tarde[0], th_tarde[1]))
        print("Noite: {} - {}".format(th_noite[0], th_noite[1]))

    try:
        csvr = csv.reader(open(csv_file))
        
        manha = []
        tarde = []
        noite = []

        for row in csvr:
            dt = datetime.strptime(row[2].strip(), '%Y-%m-%d %H:%M:%S.000')
            if th_manha[0] <= dt.hour <= th_manha[1]: # Manhã
                manha.append(row)
            elif th_tarde[0] <= dt.hour <= th_tarde[1]: # Tarde
                tarde.append(row)
            else: # Noite
                noite.append(row)

        return manha, tarde, noite

    except Exception as e:
        print(e)
#        return None, None, None


if __name__ == "__main__":
    if len(sys.argv) == 2:
        csv_filename = sys.argv[1]

        m, t, n = splitDay(csv_filename)
        if csv_filename[-3:] in ['csv', 'txt']:
            manha_fname = "{}_manha.csv".format(csv_filename[:-4])
            tarde_fname = "{}_tarde.csv".format(csv_filename[:-4])
            noite_fname = "{}_noite.csv".format(csv_filename[:-4])
            
            print("Saving {}".format(manha_fname))
            with open(manha_fname, 'w') as f:
                cw = csv.writer(f)
                for line in m:
                    cw.writerow(line)

            with open(tarde_fname, 'w') as f:
                cw = csv.writer(f)
                for line in t:
                    cw.writerow(line)

            with open(noite_fname, 'w') as f:
                cw = csv.writer(f)
                for line in n:
                    cw.writerow(line)

    else:
        print("Use {} data.csv".format(sys.argv[0]))
