#A basic script demonstrating filesystem shell methods.

import os
import shutil
from os import path
from shutil import make_archive

def main():
    #make a duplicate of an existing file
    if path.exists("textfile.txt"):
        #get the path to the file in the current directory
        src = path.realpath("textfile.txt");

        #seperate the path part from the filename
        head, tail = path.split(src)
        print "path: " + head
        print "file: " + tail

        #let's make a backup copy by appending "bak to the name"
        dst = src + ".bak"
        print dst
        #now use the shell to make a copy of the file
        shutil.copy(src,dst)

        #rename the original file
        os.rename("textfile.txt", "newfile.txt")
main()
