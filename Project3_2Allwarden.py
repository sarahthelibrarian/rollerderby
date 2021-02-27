#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import necessary libraries
import pandas as pd
import csv
import re
import numpy as np
import matplotlib.pyplot as plt



#define a dictionary with our csv names and the year they are associated with
csv_dic = {2020: "rankings_data2020.csv", 2019: "rankings_data2019.csv", 2018: "rankings_data2018.csv", 2017: "rankings_data2017.csv", 2016: "rankings_data2016.csv"}


# In[35]:


teams = []
teams_rankings = {}
data = pd.read_csv("rankings_data2020.csv", nrows=12)
for n in range(0, 12):
    teams.append(data['league'][n])

#define a function to check if a key is already in the dictionary, if not append it
def check_key(dictionary, key, value):
    #if in dictionary, change to a list if not a list type, then append value
    if key in dictionary:
        if not isinstance(dictionary[key], list):
            dictionary[key] = [dictionary[key]]
        dictionary[key].append(value)
    #otherwise just append the value
    else:
        dictionary[key] = (value)


for k, v in csv_dic.items():
    csvfile = open(v)
    #readline variable
    linesreader = csv.reader(csvfile, delimiter = ",")
    #skip the header line
    next(linesreader)
    for l in linesreader:
        #checking each csv for each team!!
        for team in teams:
            team_name = re.compile(rf'{team}', re.I)
            a = team_name.search(str(l))
            #so without the <100, we get an issue with multiple Texas teams, and multiple teams with Rainy City as a name
            #is this 'cheating'? or is it 'knowing your data'? I think... knowing your data!
            if a != None and int(l[1]) < 100:
                check_key(teams_rankings, l[2], int(l[1]))
    csvfile.close()

#2 x 4 roller derby entered WFTDA 01/2016
#they weren't ranked until september 2016 after filling in their necessary requirements, so I added this data manually
#gotta love real datasets for their quirks
check_key(teams_rankings, '2 x 4', 40)


# In[36]:


with open('top12rankings.csv', 'w', newline='') as csvfile:
    thewriter = csv.writer(csvfile)
    thewriter.writerow(['league', '2020', '2019', '2018', '2017', '2016'])
    for key, value in teams_rankings.items():
        thewriter.writerow([key, value[0], value[1], value[2], value[3], value[4]])

csvfile.close()


# In[33]:





# In[32]:





# In[ ]:




