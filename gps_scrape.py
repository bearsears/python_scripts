#scrape gps coordinates for saskatchewan wells.
#use chromedriver to login, and after that let the program rip through 
#130000 wells and store the gps coordinates in csv.

response = webdriver.request('GET', 'https://www.google.com/', 5, 5)
print(response)
print('Open another tab, and log into IRIS...')
#need to log in manually
print("Press enter as soon as you have finished")
temp = input()


with open('gpsWell20210615.csv', 'r', newline='') as csvfile, open('coord20210615.csv', 'w', newline='') as cf:
    wte = csv.writer(cf)
    line = csv.reader(csvfile)
    count = 0
    for i in line:
        if i[2] == 'Planned' or i[6] == 'Leg':
            continue
        if i[3] == 'Vertical':
            wte.writerow([i[1], i[2], i[3], i[4], i[5].split(' ')[-1], i[7], i[8]])
            continue
        print(i)
        link = "https://iris.gov.sk.ca/Portal/IRIS/Infrastructure/Well/Detail/" + i[0]
        print(link)
        res = webdriver.request('GET', link, 5, 5)  
        print(res)
        left = re.search("Latitude", res.text).start()
        right = re.search("Datum", res.text).start()
        temp = res.text[left:right]          
        lat = re.search("[0-9]{2}\.[0-9]+", temp).group()
        lng = re.search("-[0-9]{3}\.[0-9]+", temp).group()  

        print(lat, lng)
        wte.writerow([i[1], i[2], i[3], i[4], i[5].split(' ')[-1], lat, lng])
        time.sleep(1)
        print()
