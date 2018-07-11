import quandl
import pandas as pd
import numpy as np
import csv

#Extracting all the stocks and converting to a list
fIn = open('tickers.csv')
fIn.readline()
lines = fIn.read().splitlines()
tlist = []
for line in lines:
    fields = line.split(',')
    tlist.append(fields[0])

quandl.ApiConfig.api_key = "ZVTc466zs-BGkxE_s2d5"

list1=[]

for x in tlist:
    data1 = quandl.get(['NSE/%s.5'%x,'NSE/%s.6'%x], start_date='2017-01-01', end_date='2018-07-10', collapse ='daily')
    data2 = data1.to_dict(orient='split')
    data3 = data2["data"]
    data4 = data2["index"]

    cnt = 0
    for y in data3:
        dic1={}
        dic1['stock'] = x
        dic1['date'] = data4[cnt]
        dic1['price'] = y[0]
        dic1['volume'] = y[1]
        list1.append(dict(dic1))
        cnt = cnt + 1

outfile = open('QData.csv', 'w',newline='')

csvwriter = csv.writer(outfile)

count = 0

for i in list1:

      if count == 0:
             header = i.keys()
             csvwriter.writerow(header)
             count += 1

      csvwriter.writerow(i.values())
outfile.close()
