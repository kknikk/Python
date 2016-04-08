__author__ = 'kurtnikaitani'
import urllib2
import re

response = urllib2.urlopen('http://w1.weather.gov/xml/current_obs/PHNL.xml')
html = response.read()
split = html.split('\n')

tempPattern = re.compile('.*<temperature_string>.*')
humPattern = re.compile('.*<relative_humidity>.*')
windPattern = re.compile('.*<wind_string>.*')

for line in split:
    tempResult = tempPattern.match(line)
    humResult = humPattern.match(line)
    windResult = windPattern.match(line)

    if tempResult:
        substr = line[21:]
        index = substr.index('<')
        print "Current temperature: " + substr[:index]
    if humResult:
        substr2 = line[20:]
        index2 = substr2.index('<')
        print "Current relative humidity: " + substr2[:index2] + "%"
    if windResult:
        substr3 = line[14:]
        index3 = substr3.index('<')
        print "Wind is currently " + substr3[:index3]