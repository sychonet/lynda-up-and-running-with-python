#Read and write files using the built-in Python file methods

def main():
    #Open a file for writing and create it if it doesn't exist
    f = open("textfile.txt","w+")

    #Write some lines of data to the file
    for i in range(10):
        f.write("This is the line %d\n" % (i+1))

    #close the file when done
    f.close()

    #Open the file back up and read the contents
    f = open("textfile.txt","r")
    if f.mode == "r": #check to make sure that the file was opened
        #you can use the read() function to read the entire file
        #or you can use readlines() function to read the contents of file line by line
        fl = f.readlines()
        for x in fl:
            print x
    else:
        print "Unable to open file."

main()
