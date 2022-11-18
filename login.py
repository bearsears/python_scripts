#used to automate login in work website.
#obviously a lot of stuff will be editted out, 
#but it was reading the tokens in the javascript and 
#enter password manually through terminal
#worked really well until captcha.


import requests
import shutil
from bs4 import BeautifulSoup
import getpass
import csv
import re
import datetime
import os

"""
sensitive stuff omitted.
"""

with requests.session() as s: 
    
    #Retrieving necessary Form Data for Post
    res = s.get(login)
    soup = BeautifulSoup(res.content, 'lxml')
    piece = soup.find_all('input')
    postit['__VIEWSTATE'] = piece[0]['value']
    postit['__VIEWSTATEGENERATOR'] = piece[1]['value']
    postit['__EVENTVALIDATION'] = piece[2]['value']
   
    #Getting the captcha image
    image = s.get("https://iris.gov.sk.ca/Portal/Security/Credentials/CaptchaHandler.ashx", stream=True)
    with open("captcha.png", 'wb') as image_file:
        image.raw.decode_content = True
        shutil.copyfileobj(image.raw, image_file)

    postit['ctl00$mainContentPlaceHolder$uxCaptchaText'] = input("Captcha: ")
    postit['ctl00$mainContentPlaceHolder$uxPassword'] = getpass.getpass(prompt='Password: ')
    #print("the captcha is", postit['ctl00$mainContentPlaceHolder$uxCaptchaText'])
    #print(postit)
    res = s.post(url = login, data = postit)
    
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
            res = s.get("https://iris.gov.sk.ca/Portal/IRIS/Infrastructure/Well/Detail/" + i[3] + "#7")
            print(link)
            
            dates = list(set(re.findall("[2][0][0-9]{2}-[0-9]{2}-[0-9]{2}", res.text)))
            print(dates)
            for j in dates:
                temp = datetime.datetime.strptime(j, '%Y-%m-%d')
                if  temp > auth_date and temp <= datetime.datetime.today():
                    i.append(j)
                    wte.writerow(i)
                    break

#this will filter out used authorization and leaves auths.csv with unused auths

"""
    print(res.text)
    print(res.status_code)
    print(postit)
"""
    
    
    
"""
    for i in auth_type:
        res = s.get(auth_search[0] + i + auth_search[1] + str(week_before) + auth_search[2])
        temp =  list(set(re.findall("\"[0-9]{6}\"", res.text)))
        for j in temp:
            auths.append(j)
    
    #take out " " in the auth.
    for i in range(len(auths)):
        auths[i] = auths[i][1:7]
"""
            
    
"""
    link = "https://iris.gov.sk.ca/Portal/IRIS/Infrastructure/Obligations/Detail/"
    for i in range(2, 5):
        linkp = link + str(i)
        res = s.get(linkp)
        soup = BeautifulSoup(res.content, 'lxml')
        td = soup.find_all('td')
        #some obligations do not exist.
        if len(td) < 1:
            continue
        print(i)
        for i in lists:
            print(td[i].text.strip().replace("\n", " "))
"""  




