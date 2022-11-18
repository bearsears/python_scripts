# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:54:06 2020

@author: ssuh
"""
import csv

i = 0 
well_memo_lsd = set() #remember lsd
wells_cluster = dict() # will cluster in lsd and carry licence, if they are not abandoned.

inspected_memo_lsd = set()
inspected_cluster = dict()

with open('coord20200901.csv', 'r', newline='') as wells_csv, open('inspected.csv', 'r', encoding='utf8', newline='') as inspected_csv:
    wells = csv.reader(wells_csv)
    inspected = csv.reader(inspected_csv)

    for i in wells:
        #rule out abandoned wells and facilities
        if i[1] == 'ABD' or len(i[0]) < 5:
            continue
        lsd = i[2][6:]
        #print(lsd, i[0], end='\t\t\t\t\t')
        if lsd in well_memo_lsd:
            wells_cluster[lsd].add(i[0])
        else:
            wells_cluster[lsd] = set()
            wells_cluster[lsd].add(i[0])
            well_memo_lsd.add(lsd)


    for i in inspected:
        #for empty row, or anything that can cause trouble
        if len(i) < 6:
            continue
        
        lsd = i[5][6:]
        temp = i[11].split('"')
        #print(temp)
        licence = i[11].split('"')
        #print(licence[1], end='\t')
        licence = licence[1]
        if len(licence) < 5 or "SK" in licence or "PL" in licence:
            continue
        if lsd in inspected_memo_lsd:
  
            inspected_cluster[lsd].add(licence)
        else:
            #print(i, temp)
            inspected_cluster[lsd] = set()
            inspected_cluster[lsd].add(licence)
            inspected_memo_lsd.add(lsd)

#print(memo_lsd)

"""
for i in inspected_cluster:
    print(i, inspected_cluster[i])
""" 
""" 
for i in wells_cluster:
    print(i, wells_cluster[i])
"""

uninspected = dict()


total_uninspected, total_well = 0, 0
lloyd_uninspected, lloyd_well = 0, 0

for i in wells_cluster:
    
    if not i in inspected_memo_lsd:
        uninspected[i] = set()
        continue
            
    uninspected[i] = wells_cluster[i].difference(inspected_cluster[i])
    #print(int(i[:3]))
    if i == '048-21W3':
        print(uninspected[i])
        print(inspected_cluster[i])
        print(wells_cluster[i])
    
    twp = int(i[:3])
    
    lun, lwe = len(uninspected[i]), len(wells_cluster[i])
    print(i, lun, lwe)
    total_uninspected += lun
    total_well += lwe
    if twp >= 38:
        lloyd_uninspected += lun
        lloyd_well += lwe
        
    if lun / lwe > 0.5:
        print(i, lun, lwe, lun / lwe)  
    
    
print(total_uninspected, total_well, total_uninspected / total_well)
print(lloyd_uninspected, lloyd_well, lloyd_uninspected / lloyd_well)
print(total_uninspected - lloyd_uninspected, total_well - lloyd_well, (total_uninspected - lloyd_uninspected) / (total_well - lloyd_well))

