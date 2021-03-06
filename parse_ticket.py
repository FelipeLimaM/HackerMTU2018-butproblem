import csv, json
from datetime import datetime


with open('dados_bilhetagem_RMBS_Onibus.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    frequency = {}
    next(spamreader)
    list_VT = []
    for row in spamreader:
        # 2016-10-07 16:07:24.00
        if row[8] == "V.T.":
            row[2] = datetime_object = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.000')
            if row[1] in frequency:
                if  str(row[2].date()) in frequency[row[1]]:
                    frequency[row[1]][str(row[2].date())]["count"]+=1
                    frequency[row[1]][str(row[2].date())]["list"].append(row)
                else:
                    frequency[row[1]][str(row[2].date())]={"count":1,"list":[row]}
            else:
                frequency[row[1]] = {str(row[2].date()) :{"count":1,"list":[row]}}


    # step 2
    print "step2"
    # with open('output.json', 'w') as outfile:
    #     json.dump(frequency, outfile)

    for i in frequency.keys():
        for date in frequency[i].keys():
            if frequency[i][date]["count"] == 2:
                list_VT.append(frequency[i][date]["list"][0])
                list_VT.append(frequency[i][date]["list"][1])


    with open("outputfile.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
#        field = ["RM,"cartao","uso_datahora","Linha","Sentido","tipo_embarque","prefixo","aplicacao","Desc_Aplic","TipoPassagem"]
#        writer.writerow(field)
        for i in xrange(0,len(list_VT),2):
            list_VT[i][2] = str( list_VT[i][2] )

            writer.writerow(list_VT[i])
