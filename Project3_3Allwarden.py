#import necessary libraries

import csv, re, random, pandas as pd


#all of this is done in order to clean the GPA data, so there are no commas and can be converted to floats!

#initialize empty data 
#getting boston's data at the same time
boston_data = []
gpa = []

#find Boston's data and get clean data. This is the data pulling stage
csvfile = open('rankings_data2020.csv')
#readline variable
linesreader = csv.reader(csvfile, delimiter = ",")
#skip the header line
next(linesreader)
#search for boston using reg ex
boston = re.compile(r'Boston', re.I)
for l in linesreader:
    a = boston.search(str(l))
    if a != None:
        #once found append data to our list variable
         boston_data.append({"rank": l[1], "gpa": l[3], "weight": l[4]})
    gpa.append(l[3])
#make it a true dictionary for easier access
boston_data = boston_data[0]
#open up a data frame for ease
df = pd.read_csv("rankings_data2020.csv", delimiter = ",")
clean_gpa = ['gpa']
for i in gpa:
    a = i
    a = a.replace(',', '')
    clean_gpa.append(float(a))

#close the file so I can mess with it again later
csvfile.close()

#this is the data cleaning stage

#this function allows us to change our csv: https://thispointer.com/python-add-a-column-to-an-existing-csv-file/
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append/insert a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = csv.reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)
        read_obj.close()
        write_obj.close()

#deleting the bad data https://stackoverflow.com/questions/7588934/how-to-delete-columns-in-a-csv-file
#reading in our rankings data csv
with open("rankings_data2020.csv","r") as source:
    rdr= csv.reader(source)
    #creating our new csv that doesn't have the column
    with open("no_gparankings_data2020.csv","w") as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow((r[0], r[1], r[2], r[4]))
source.close()
result.close()

#inserting our new column int our clean data!
add_column_in_csv('no_gparankings_data2020.csv', 'cleanrankings_data2020.csv', lambda row, line_num: row.insert(3, clean_gpa[line_num - 1]))

#reading our dataframe from our clean data so we can do our game!
df = pd.read_csv("cleanrankings_data2020.csv", delimiter = ",")

#INSTRUCTIONS FOR OUR GAME
print("Congrats! You've been drafted to the Boston Massacre, the A-team for Boston Roller Derby ranked 36 in the world. It's going to be a great season!")
print("When you're ready, type Yes or yes!")
print("When you need a break, type Stop or stop!")
ready = input("Are you ready to play? ")

#while loop
while ready == 'Yes' or ready == 'yes':
    #get random ranking to generate other opponent
    opp_rank = random.randint(1, 351)
    #parse that data for information on our other team
    opp_team = df.loc[df['rank'] == opp_rank]
    opp_team_name = opp_team['league']
    opp_weight = float(opp_team['weight'])
    opp_gpa = opp_team['gpa']
    opp_gpa = opp_gpa.replace(',', '')
    opp_gpa = float(opp_gpa)
    
    #separate out our boston data... I know I could do this all at once later but it hurts my brain to do it like that, even though it makes more code this way
    #i think it's easier to read
    bos_gpa = float(boston_data['gpa'])
    bos_weight = float(boston_data['weight'])
    
    #generate some random scores!! woooooo
    bos_score = float(random.randint(5, 500))
    opp_score = float(random.randint(5, 500))
    
    #calculate the actual game points using the complicated WFTDA equation
    bos_gp = (bos_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    opp_gp = (opp_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    
    #give our player some information and separate it out just for usability
    print("You are playing " + opp_team_name)
    print("They are ranked: " + str(opp_rank))
    print("Are you done warming up?")
    lets_go = input("Type Yes if you're ready to play! ")
    
    if lets_go == 'Yes' or lets_go == 'yes':
        #scenario 1, you won!
        if bos_score > opp_score:
            #give user information
            print("Boston won! And you got awarded MVP! The final score was " + str(bos_score) + " vs " + str(opp_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            #scenario 1 part a
            if gpa_change > 0:
                #best thing that could happen! 
                print('GPA change was: ' + str(gpa_change))
                print("Your GPA was positively affected by this game, meaning you will likely go up in rankings! Yay! You killed it!")
                #scenario 1 part b
            elif gpa_change < 0:
                #this isn't ideal, even though you 'won' your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, even though you won, your GPA was negatively affected by this game. You could end up going down in the rankings. There will be other games, though!")
        
        #scenario 2, you lost
        elif opp_score > bos_score:
            print("Oh no, you lost. You played great, though! The final score was " + str(opp_score) + " vs " + str(bos_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            
            #scenario 2 part a
            if gpa_change > 0:
                #if you lose, this is still good!!
                print('GPA change was: ' + str(gpa_change))
                print("Even though you lost, your GPA was positively affected by this game, meaning you will could go up in rankings! Yay! You killed it!")
            #scenario 2 part b
            elif gpa_change < 0:
                #your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, your GPA was negatively affected by this game. You could end up going down in the rankings. There will be other games, though!")
    #decide if we want to come out of our loop  
    ready = input("Are you ready to play? ")

#close out the game 
if ready == "Stop" or ready == "stop":
    print("Thanks for playing! Congrats on your first season with the Boston Massacre.")

#another version
#this one is more like a tool, for someone to do theoretical scores

#INSTRUCTIONS FOR OUR GAME
ready = input("Are you ready to test some scores? ")

#while loop
while ready == 'Yes' or ready == 'yes':
    #get random ranking to generate other opponent
    opp_rank = int(input("What is the team rank? "))
    #parse that data for information on our other team
    opp_team = df.loc[df['rank'] == opp_rank]
    opp_team_name = opp_team['league']
    opp_weight = float(opp_team['weight'])
    opp_gpa = opp_team['gpa']
    opp_gpa = opp_gpa.replace(',', '')
    opp_gpa = float(opp_gpa)
    
    #separate out our boston data... I know I could do this all at once later but it hurts my brain to do it like that, even though it makes more code this way
    #i think it's easier to read
    bos_gpa = float(boston_data['gpa'])
    bos_weight = float(boston_data['weight'])
    
    #have user insert in theoretical scores!
    bos_score = float(input("What is Boston's score? "))
    opp_score = float(input("What is the opposition's score? "))
    
    #calculate the actual game points using the complicated WFTDA equation
    bos_gp = (bos_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    opp_gp = (opp_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    
    #give our player some information and separate it out just for usability
    print("You are playing " + opp_team_name + " they are ranked: " + str(opp_rank))
    print("Ready to see the results?")
    lets_go = input("Type Yes ")
    
    if lets_go == 'Yes' or lets_go == 'yes':
        #scenario 1, you won!
        if bos_score > opp_score:
            #give user information
            print("Boston won! The final score was " + str(bos_score) + " vs " + str(opp_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            #scenario 1 part a
            if gpa_change > 0:
                #best thing that could happen! 
                print('GPA change was: ' + str(gpa_change))
                print("Your GPA was positively affected by this game")
                #scenario 1 part b
            elif gpa_change < 0:
                #this isn't ideal, even though you 'won' your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, even though you won, your GPA was negatively affected by this game. You could end up going down in the rankings. ")
        
        #scenario 2, you lost
        elif opp_score > bos_score:
            print("Oh no, you lost.  The final score was " + str(opp_score) + " vs " + str(bos_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            
            #scenario 2 part a
            if gpa_change > 0:
                #if you lose, this is still good!!
                print('GPA change was: ' + str(gpa_change))
                print("Even though you lost, your GPA was positively affected by this game.")
            #scenario 2 part b
            elif gpa_change < 0:
                #your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, your GPA was negatively affected by this game. You could end up going down in the rankings.")
    #decide if we want to come out of our loop  
    ready = input("Are you ready to test some scores? ")