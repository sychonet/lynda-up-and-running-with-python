#A simple script demonstrating fetching and processing of JSON data from a URL using Python script

import urllib2
import json

def printResults(data):
    #Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    #now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]

    print

    #output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"

    print

    #for each event, print the place where it occurred
    for i in theJSON["features"]:
        print i["properties"]["place"]

    print

    #print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

    print

    #print only the events where at least 1 person reported feeling something
    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"

def main():
    #define a variable to hold the source URL
    #In this case we'll use the free data feed from the USGS
    #This feed lists all earthquakes for the last day larger than Mag 2.5

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib2.urlopen(urlData)
    print str(webUrl.getcode()) + "\n"

    if (webUrl.getcode() == 200):
        data = webUrl.read()
        #print out our customized results
        printResults(data)
    else:
        print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())

main()
