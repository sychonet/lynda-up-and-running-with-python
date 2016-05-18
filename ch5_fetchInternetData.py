#A simple script demonstrating the use of urllib2 to fetch data from Internet using Python script

import urllib2

def main():
    #Open a connection to a URL using urllib2
    webUrl = urllib2.urlopen("http://robocop.io")

    #get the result code and print it i.e. HTTP Response code as 200,404 etc.
    print "result code:" + str(webUrl.getcode())

    #read the data from the URL and print it
    data = webUrl.read()
    print data
    
main()
