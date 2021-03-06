# -*- coding: utf8 -*-

# This program reads a Thomson Reuters Web of Science(TM) file
# and creates a histogram for the number of articles published
# per year. It should work with any file following the ISI format. 

from sys import argv
import numpy as np
import re
import matplotlib.pyplot as plt


# Printing an error messag in case the user forgets filename. 
print '-' * 10
print 'USAGE: python WOSyears.py filename'
print '_' * 10

# Opening and reading the file selected by the user. 
script, filename = argv
f = open(filename)
wosrecords = f.read()

# Counts the articles in the dataset.
# Number of articles (PT) should match years (PY). 
def articlecount():
    result = re.findall(r'^PT', wosrecords, flags = re.MULTILINE)
    articles = len(result)
    return articles

# Defining the regular expression to extract the PY field (publication year). 
def findyears():
    result = re.findall(r'^PY (\d\d\d\d)', wosrecords, flags = re.MULTILINE)
    return result

years = findyears()

# Creating a list of years.
plotyears = []

# Appending the years to the list above. 
for y in years:
    plotyears.append(y)

# Converting string to integer value. 
intplotyears = [int(i) for i in plotyears]

# Defining how many years to plot
totalyearcount = len(intplotyears)

# Print out statistics for verification and finding 
# possible errors in plotted graph.
# print "\nThe years are:\n\n %s" % intplotyears   # print all years. 
print "\nIn %s records (PT), %s years (PY) were found.\n" % (articlecount(), totalyearcount)
peryear = [[x,intplotyears.count(x)] for x in set(intplotyears)]
print "For each year, the following amounts of articles were published:\n %s" % peryear
print "\nPlotting graph..."
print "Saving output as 'YEARLY.pdf'..."
print "Close pop up window to return to shell."


# Create and show histogram, save as pdf
plt.hist(intplotyears, 
        np.arange(min(intplotyears), max(intplotyears) + 2), #This adds some unnecessary space. 
        facecolor='green'
        )
plt.xlabel('Years')
plt.ylabel('Number of articles')
plt.savefig('YEARS.pdf')   #change this to .png or .svg
plt.show()


