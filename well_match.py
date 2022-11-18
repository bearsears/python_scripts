#nice and quick script to update csv data

import csv


with open('gpsWell20191203.csv', 'r', newline='') as csvfile, open('gpsWell.csv', 'r', newline='') as csvfile1, open('gpsWell20200901.csv', 'w', newline='') as cf:
    wte = csv.writer(cf)
    line =  csv.reader(csvfile)
    line1 = csv.reader(csvfile1)
    count = 0
    for i in line:
        jcount = 0
        for j in line1:
            if i[0] == j[0]:
                wte.writerow([j[0], j[1], j[2], j[4], i[5], i[6], i[7]])
                break
            else:
                wte.writerow([j[0], j[1], j[2], j[4], j[5][6:20], '', ''])
