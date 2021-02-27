#import necessary libraries
import pandas as pd, csv, numpy as np, matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#our data needs to be laid out differently, so use pandas to transpose
pd.read_csv('top12rankings.csv', header=None).T.to_csv('transpose_top12rankings.csv', header=False, index=False)

#read transposed data
data = pd.read_csv('transpose_top12rankings.csv')

# Make a data frame from our data to put into our chart
#sample code from: https://python-graph-gallery.com/125-small-multiples-for-line-chart/
data = pd.read_csv('transpose_top12rankings.csv')
df=pd.DataFrame({'x': data['league'], 'Rose City': data['Rose City'], 'Victoria': data['Victoria'], 'Gotham': data['Gotham'], 'Denver': data['Denver'], 'Arch Rival': data['Arch Rival'], 'Montréal': data['Montréal'], 'Texas': data['Texas'], 'Angel City': data['Angel City'], 'Philly': data['Philly'], 'Rainy City': data['Rainy City'] , '2 x 4': data['2 x 4'], 'Helsinki': data['Helsinki'] })

# Initialize the figure
plt.style.use('seaborn-darkgrid')

#make it bigger!
figure(figsize=(6, 5))
# multiple line plot
num=0
for column in df.drop('x', axis=1):
    num+=1

    
    
    # Find the right spot on the plot
    plt.subplot(4,3, num)
    
    # plot every groups, but discreet
    for v in df.drop('x', axis=1):
        plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
        
        
    # Plot the lineplot
    plt.plot(df['x'], df[column], marker='', color= 'purple', linewidth=2.4, alpha=0.9, label=column)
    
    
    # Same limits for everybody!
    plt.xlim(2016, 2020)
    plt.ylim(0,100)
 
 
 
    # Add title
    plt.title(column, loc='left', fontsize=8, fontweight=0, color='purple' )
    
#general title

plt.suptitle("How have rankings changed over the past 5 years?", fontsize=13, fontweight=0, color='black', style='italic')
 
# Axis title
plt.text(0.5, 0.02, 'Years', ha='center', va='center')
plt.text(0.06, 0.5, 'Rankings', ha='center', va='center', rotation='vertical')

#save the figure
plt.savefig('Project3_2Allwarden.png')
#show the figure
plt.show()