#A basic script demonstrating use of classes in Python programming language

class myClass():
  def method1(self):
    print "myClass method1"

  def method2(self, someString):
    print "myclass method2: " + someString

#Inheritance example
class anotherClass(myClass):
    #Overriding example
    def method2(self):
        print "anotherClass method2"

    def method1(self):
        myClass.method1(self)
        print "anotherClass method1"

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()
main()
