#to check if authenticating has been used or not.


#This script will get html from selenium-request
#where to start?

import csv, re, datetime, os
from seleniumrequests import Chrome


webdriver = Chrome()
response = webdriver.request('GET', 'https://www.google.com/', 5, 5)
print(response)
print("Press enter as soon as you have finished")
temp = input()

with open('auths.csv', 'r', newline='') as csvfile, open('auths_used.csv', 'a', newline='') as cf:
    wte = csv.writer(cf)
    line = csv.reader(csvfile)
    for i in line:
        #print(i[2], line.line_num, end='\t')
        #print(datetime.datetime.strptime(i[2], '%m/%d/%Y').strftime('%Y-%m-%d'))
        auth_date = datetime.datetime.strptime(i[2], '%m/%d/%Y')
        #if i[4] == 'Lloydminster':
        #    wte.writerow(i)
        
        link = "https://iris.gov.sk.ca/Portal/IRIS/Infrastructure/Well/Detail/" + i[3] + "#7"
        print(link)
        res = webdriver.request('GET', link, 5, 5)  
        print(res)
        
        dates = list(set(re.findall("[2][0][0-9]{2}-[0-9]{2}-[0-9]{2}", res.text)))
        print(dates)
        for j in dates:
            temp = datetime.datetime.strptime(j, '%Y-%m-%d')
            if  temp > auth_date and temp <= datetime.datetime.today():
                i.append(j)
                wte.writerow(i)
                break

with open('auths.csv', 'r', newline='') as csvfile, open('auths_used.csv', 'r', newline='') as csvfile1, open('auths_temp.csv', 'w', newline='') as cf:
    wte = csv.writer(cf)
    line =  csv.reader(csvfile)
    line1 = csv.reader(csvfile1)
    line1_array = []
    for j in line1:
        line1_array.append(j[0])
        

    for i in line:
        if not i[0] in line1_array:
            #print(i, line.line_num)
            wte.writerow(i)

    #print(line1_array)
os.remove('auths.csv')
os.rename('auths_temp.csv', 'auths.csv',)
