#Returns all files created after inputted date in the current directory
__author__ = 'kurtnikaitani'

import time
import os
import datetime

# Obtain input of current date with exception handling for format
def obtainDate():
    isValid = False
    while not isValid:
        input1 = raw_input("Enter a creation date in the format MM/DD/YYYY hh:mm:ss - ")
        fmt = "%m/%d/%Y %H:%M:%S"
        try:
            date = datetime.datetime.strptime(input1, fmt).strftime(fmt)
            #date = date.strfttime(fmt)
            isValid = True
        except ValueError as err:
            print("Error: Please use the correct format.")
    return date


createDate = obtainDate()

print "Files created after " + createDate + " - \n"

# Set current dir
path = os.getcwd()
dirs = os.listdir(path)


for fi in dirs:
   fmt = "%m/%d/%Y %H:%M:%S"
   compare = datetime.datetime.strptime(time.ctime(os.path.getctime(fi)), "%a %b %d %H:%M:%S %Y").strftime(fmt)
   if compare >= createDate:
      print fi + " created: %s" % compare