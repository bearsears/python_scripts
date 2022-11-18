#this is to showcase that I know how to use regex.


import csv
import re
from seleniumrequests import Chrome
import time

webdriver = Chrome()
response = webdriver.request('GET', 'https://www.google.com/', 5, 5)
print(response)
#need to log in manually
print("Press enter as soon as you have finished")
temp = input()

with open('facilities.csv', 'r', newline='') as csvfile, open('facilities_updated.csv', 'w', newline='') as cf:
    wte = csv.writer(cf)
    line = csv.reader(csvfile)
    count = 0
    for i in line:
        if len(i) == 6 and len(i[4]) > 5:
            wte.writerow(i)
            continue        
        print(i)
        link = "https://iris.gov.sk.ca/Portal/IRIS/Infrastructure/FacilitySite/FacilitySite?licenceNumber=" + i[0] + "&authorizationNodeType=F"
        print(link)
        res = webdriver.request('GET', link, 5, 5)  
        print(res)
        left = re.search("DLS", res.text).start()
        right = re.search("Datum", res.text).start()
        temp = res.text[left:right]          
        lsd = re.search("[0-9]+-[0-9]+-[0-9]+-[0-9]+W[123]", temp).group()
        lat = re.search("[0-9]{2}\.[0-9]+", temp).group()
        lng = re.search("-[0-9]{3}\.[0-9]+", temp).group()  
        if len(i) == 2:     
            i.append(lsd)
            i.append(lsd)
            i.append(lat)
            i.append(lng)
        else:
            i[4] = lat
        print(i)
        wte.writerow(i)
        time.sleep(1)
        print()
