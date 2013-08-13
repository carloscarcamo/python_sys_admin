#! /usr/bin/env python

import subprocess

#command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

#command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information with %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

#main function that call other functions
def main():
    uname_func()
    disk_func()

#execute main function
main()
