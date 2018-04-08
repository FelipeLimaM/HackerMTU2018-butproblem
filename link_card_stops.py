import csv
from math import sqrt


def link_items(output):
    with open(output, 'w') as csvfile:
        writer = csv.writer(csvfile)
        with open('data/RMBS_stops.txt', 'rb') as stops:
            stopsreader = list(csv.reader(stops, delimiter=',', quotechar='\n'))
            with open('data/RMBS_bilhetagem_coord_line_904_bus_8611.txt', 'rb') as cards:
                cardsreader = list(csv.reader(cards, delimiter=',', quotechar='\n'))
                for i in cardsreader:
                    distance_i = sqrt( (float(stopsreader[0][2]) - float(i[10]))**2 + (float(stopsreader[0][3]) - float(i[11]))**2 )
                    line = stopsreader[0]
                    for j in stopsreader:
                        # print float(j[2]) ,float(i[10]) , float(j[3]) , float(i[11])
                        distance_here = sqrt( (float(j[2]) - float(i[10]))**2 + (float(j[3]) - float(i[11]))**2 )
                        if distance_here < distance_i:
                            distance_i = distance_here
                            line = j

                    i[10] = line[2]
                    i[11] = line[3]
                    writer.writerow(i)

link_items("data_cards_stops.csv")
