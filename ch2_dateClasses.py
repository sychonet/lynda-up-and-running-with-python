#A basic script demonstrating use of date, time and datetime classes in Python

#In the following import statements datetime is an inbuilt module in Python and date,time and datetime are classes from module that need to be imported
from datetime import date
from datetime import time
from datetime import datetime

def main():
    #DATE OBJECTS
    #Get today's date from the simple today() method from the date class
    today = date.today()
    print "Today's date is ", today

    #print out the date's individual components
    print "Date Components: ", today.day, today.month, today.year

    #retrieve today's weekday (0=Monday, 6=Sunday)
    print "Today's Weekday #: ", today.weekday()

    print " "

    #DATETIME OBJECTS
    #Get today's date from the datetime class
    today1 = datetime.now()
    print "The current date and time is ", today1

    #Get the current time
    t = datetime.time(today1)
    print "The current time is ",t

    #weekday returns 0 (monday) through 6(sunday)
    wd = date.weekday(today1)
    #Days start from 0 for Monday
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print "Today is day number %d" % wd
    print "Which is a " + days[wd]

main()
