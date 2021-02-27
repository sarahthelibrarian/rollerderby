#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import necessary libraries
import csv
import requests
#this is used for web scraping
from bs4 import BeautifulSoup

#took the idea from https://github.com/bgreman/derby-stats-scraper/blob/master/python/rankings_scraper.py 
#made it into a function so i could pull multiple urls without repeating code
def rankings_puller(stats_url, a):
    #this will be our url
    stats_url = stats_url
    #this is the year our data is from
    year = a
    #getting the data
    resp = requests.get(stats_url)
    #parsing the data
    soup = BeautifulSoup(resp.content, 'html.parser')
    #making it readable
    rankings_table = soup.find(class_="rankingsTable")
    rankings_body = rankings_table.tbody
    #making sure data can be called outside of the function
    global data
    data = []
    #iterating through all of our data and appending it to the data list
    for row in rankings_body.contents[1:None:2]:
        year = year
        rank = row.find(class_="rankingsTable--position").string.strip()
        league = row.find(class_="rankingsTable--leagueTitleColumn").a.string.strip()
        gpa_td = row.find(class_="rankingsTable--gpa")
        gpa = next(gpa_td.strings).strip()
        weight = gpa_td.span.string.strip()
        data.append({"year": year, "rank": rank, "league": league, "gpa": gpa, "weight": weight})
    #just make sure our data looks right
    print(f"Total # of items: {len(data)}")
    


# In[8]:


#2020 data
url2020 = 'https://stats.wftda.com/rankings?r=3227'
#call function
rankings_puller(url2020, 2020)
#writing our 2020 csv
with open('rankings_data2020.csv', 'w', newline='') as csvfile:
    #title row
    fieldnames = ['year', 'rank', 'league', 'gpa', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #writing data from our dictionary
    for item in data:
        writer.writerow(item)


# In[9]:


#2019 data
url2019 = "https://stats.wftda.com/rankings?r=2453"
#call function
rankings_puller(url2019, 2019)
#writing our 2019 csv
with open('rankings_data2019.csv', 'w', newline='') as csvfile:
    #title row
    fieldnames = ['year', 'rank', 'league', 'gpa', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for item in data:
        writer.writerow(item)

#2018 data 
url2018 = "https://stats.wftda.com/rankings?r=2443"
#call the function
rankings_puller(url2018, 2018)
#writing our 2018 csv
with open('rankings_data2018.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'rank', 'league', 'gpa', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)
#2017 data      
url2017 = "https://stats.wftda.com/rankings?r=2434"
#call the function
rankings_puller(url2017, 2017)
#write to our 2017 csv
with open('rankings_data2017.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'rank', 'league', 'gpa', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)
#2016 data
url2016 = "https://stats.wftda.com/rankings?r=2425"
#call the function
rankings_puller(url2016, 2016)
#write to our 2016 csv
with open('rankings_data2016.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'rank', 'league', 'gpa', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)


# In[ ]:




