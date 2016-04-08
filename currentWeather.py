#Retrieves current weather report for Honolulu,HI
__author__ = 'kurtnikaitani'

import urllib2
import re

response = urllib2.urlopen('http://w1.weather.gov/xml/current_obs/PHNL.xml')
html = response.read()


split = html.split("\n")
pattern = re.compile(".*<weather>.* ")
for line in split:
    result = pattern.match(line)
    if result:
        substring = line[10:]
        index = substring.index('<')
        print substring[:index]
