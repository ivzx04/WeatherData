#!/usr/bin/python

from subprocess import Popen, PIPE

def convertFtoC(tempF):
    tempC = (tempF  -  32.) *  5.0 / 9.0      
    return tempC


print '\n Hello there -- Ready to get the weather data? \n'

year = raw_input("What year? ")
month = raw_input("What month? ")
day = raw_input("What day? ")

url = 'http://www.wunderground.com/history/airport/KBED/%s/%s/%s/DailyHistory.html'%(year,month,day)

parameters = '&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
fullUrl = url + '?' + parameters

cmd = 'wget'
cmdParameter1 = "-O-"
cmdParameter2 = "-q"

print ' CMD: ' + cmd + '\n PAR1: ' + cmdParameter1 + '\n PAR2: ' + cmdParameter2 + '\n URL: ' + fullUrl + '\n'
output = Popen([cmd,cmdParameter1,cmdParameter2,fullUrl],stdout=PIPE)
#print output.stdout.read()


print '\n Analyzing the data \n'

lineIt = iter(output.stdout.readline, b"")
for line in lineIt:
    
    line = line[:-7]
    ## print " LINE -- " + line

    # extract infromation from this line
    g = line.split(',')

    if len(g) > 2:
        time = g[0]
        try:

            tempF = float(g[1])
            dewPointF = float(g[2])

            tempC = convertFtoC(tempF)
            dewPointC = convertFtoC(dewPointF)

            print " %8s %7.2f F (%7.2f C) %7.2f F (%7.2f C) "%(time,tempF,tempC,dewPointF,dewPointC)

        except:
            #print ' ERROR decoding'
            pass

