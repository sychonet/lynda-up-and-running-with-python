#A simple script demonstrating variable usage in Python language.

f = 0
print f

g = "abc"
print g

def main():
    f = "def"
    print f

main()

print f

def main2():
    global f
    f = "def"
    print f

main2()

print f

print "string type " + str(123)

del f
print f
