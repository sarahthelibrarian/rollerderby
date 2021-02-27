
#import necessary libraries
import pandas as pd
import csv

#define a dictionary with our csv names and the year they are associated with
csv_dic = {2020: "rankings_data2020.csv", 2019: "rankings_data2019.csv", 2018: "rankings_data2018.csv", 2017: "rankings_data2017.csv", 2016: "rankings_data2016.csv"}


#define a wild function so I don't have to rewrite it 5 times takes the value and key from our dictionary as arguments
#it makes our code look sort of backward but stick with me
def csv_parser(csv_string, year):
    #use pandas to only read the first 12 lines of each csv
    data = pd.read_csv(csv_string, nrows=12)
    #empty list variables so we can format into table
    rank = [] 
    league = []
    gpa = []
    weight = []
    
    #only go to 12, so we do a range loop
    for n in range(0, 12):
        #get the data from our pandas and append to list
        rank.append(data['rank'][n])
        league.append(data['league'][n])
        gpa.append(data['gpa'][n])
        weight.append(data['weight'][n])
    
    #html code to write an html table for each csv
    #title for each table
    html.write("<h2>" + str(year) +"</h2>")
    #bootstrap class for a table
    html.write("<table class = 'table'>\n")
    #define the beginning and table head
    html.write("<tr><th scope = 'col'>Rank</th>\n<th scope = 'col'>League</th>\n")
    html.write("<th scope = 'col'>GPA</th>\n<th scope = 'col'>Weight</th></tr>")
    #iterate through our lists, and write out our table data
    for n in range(0, len(rank)):
        html.write("<tr>\n")
        html.write("<td>" + str(rank[n]) + "</td>\n")
        html.write("<td>" + league[n] + "</td>\n")
        html.write("<td>" + str(gpa[n]) + "</td>\n")
        html.write("<td>" + str(weight[n]) + "</td>\n")
        html.write("</tr>\n")

    html.write("</table>")



#ok now this is the section of the code where we call our functions so, we define the beginning of our html
#open our html file
html = open("Project3_1Allwarden.html", "w")
#bootstrap stylesheet info because I like to be fancy
html.write("<!DOCTYPE html><html lang='en'>\n<head><meta charset='utf-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1'>")
html.write("\n<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>")
html.write('\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
html.write('\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>')
html.write('\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>')
html.write("""\n</head><html>\n
<div class="container">\n
<body>\n
<div class="jumbotron text-center" style="margin-bottom:20px;">\n
  <h1>Final Project: Part 1</h1>\n
</div>\n""")
#first row
html.write("<div class ='row'>")
#first column
html.write('<div class="col-sm-12">')
###CALL THE FUNCTION
csv_parser(csv_dic[2020], 2020)
#close row and column
html.write('</div>')
html.write('</div>')

#second row
html.write("<div class ='row'>")
#column
html.write('<div class="col-sm-6">')
#CALL THE FUNCTION AGAIN
csv_parser(csv_dic[2019], 2019)
#close the column, not the row yet
html.write('</div>')
#open another column
html.write('<div class="col-sm-6">')
#CALL THE FUNCTION AGAIN
csv_parser(csv_dic[2018], 2018)
#close column
html.write('</div>')
#close row
html.write('</div>')

#thirdrow
html.write("<div class ='row'>")
#column
html.write('<div class="col-sm-6">')
#CALL THE FUNCTION AGAIN
csv_parser(csv_dic[2017], 2017)
#close the column, not the row yet
html.write('</div>')
#open another column
html.write('<div class="col-sm-6">')
#CALL THE FUNCTION AGAIN
csv_parser(csv_dic[2016], 2016)
#close column
html.write('</div>')
#close row
html.write('</div>')

#close the container div
html.write('</div>')
#close tags
html.write("</body>\n</html>")


#close the file
html.close()





