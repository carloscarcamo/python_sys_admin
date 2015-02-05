#! /usr/bin/env python

import subprocess

#command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])
    #another way to do it
    #subprocess.call("uname -a", shell=True)

#command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information with %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])
    #another way to do it
    #subprocess.call("df -h", shell=True)

#main function that call other functions
def main():
    uname_func()
    disk_func()

#call main function only when it is excecuted from the command line
if __name__ == "__main__":
    main()
