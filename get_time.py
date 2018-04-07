#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json, csv

def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq


def get_time(coords1,coords2):
    key = "AIzaSyB5gv9cB0ki8vaMIE2k6x_YPdZdYni655g"
    response = []
    for block in split_seq(coords1,int(len(coords1)/30)):
        origen = ""
        for i in block:
            origen+= str(i[0])+","+str(i[1])+"|"
        origen = origen[:len(origen)-1]
        destinations = ""
        for i in coords2:
            destinations+= str(i[0])+","+str(i[1])+"|"
        destinations = destinations[:len(destinations)-1]
        while True:
            url_full = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origen+"&destinations="+destinations+"&key="+key
            # print url_full
            r = requests.get(url_full)
            print r.content
            if (r.content).find("OVER_QUERY_LIMIT")==-1:
                response_json = json.loads(r.content)
                response_cache = []
                for i in response_json["rows"]:
                    try:
                        response_cache.append(i["elements"][0]["duration"]["value"])
                    except Exception as e:
                        response_cache.append(9999999)
                break
            else:
                key = raw_input("insert new key:")

        response+=response_cache
    return response



def magic(input,output):
    with open(input, 'rb') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
        with open(output, 'w') as csvfile:
            writer = csv.writer(csvfile)
            field = ["id_location","id_location", "time"]
            writer.writerow(field)
            for i in xrange(0,len(spamreader)):
                print i
                list_time = get_time(spamreader,[spamreader[i]])
                for j in xrange(0,len(list_time)) :
                    writer.writerow([str(i),str(j),str(list_time[j])])






# print get_time([[-22.811183,-47.069193],[-22.815559,-47.059656]],[[-22.808200, -47.071758]])

magic("RBMS_line_904_bus_8611_freq_filtered.txt", "input_matheus.csv")
