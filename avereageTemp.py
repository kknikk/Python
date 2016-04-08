#Retrieves the current temperature of Honolulu,HI and writes it to a text file. Prints out an avereage temperature based on data stored in text file.
__author__ = 'kurtnikaitani'
import urllib2
import re

response = urllib2.urlopen('http://w1.weather.gov/xml/current_obs/PHNL.xml')
html = response.read()
split = html.split('\n')

tempPattern = re.compile('.*<temp_f>.*')

for line in split:

    tempResult = tempPattern.match(line)

    if tempResult:
        substr = line[9:]
        index = substr.index('<')
        substr = substr[:index]
        printSubstr = "Current temperature is " + substr[:index] + " F"
        print printSubstr

# create file and append current temp
fileName = "de23.txt"
with open(fileName,'a') as myfile:
    myfile.write(substr + "\n")
    myfile.close()

def average():

    total = 0.0
    length = 0.0
    average = 0.0

    fileName = "de23.txt"
    infile = open(fileName, 'r')

    # read values and compute average
    for line in infile:
        amount = float(line.rstrip("\n"))
        total += amount
        length = length + 1

    average = total/length

    infile.close()

    print "Based on stored data in \"de23.txt\" the average temperature is " + format(average, ',.2f') + " F"

average()
