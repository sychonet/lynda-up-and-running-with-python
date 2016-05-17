#A simple script demonstrating application of loops in Python.

def main():
    x = 0
    # define a while loop
    while (x < 5):
        print x
        x = x + 1

    print  " "

    y = 0
    #define a for loop
    for y in range(10,15):
        print y

    print " "

    #use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print d

    print " "

    #use the break and continue statements
    z = 0
    for z in range(5,10):
        #if (z==7): break
        if(z % 2 == 0): continue
        print z

    print " "

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print i, d
main()
