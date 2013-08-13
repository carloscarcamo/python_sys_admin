#! /usr/bin/env bash

#A system information gathering sctipt

#command 1 
UNAME = "uname -a"
printf "Gathering system information with the $UNAME command: \n\n"
$UNAME

#command 2
DISKSPACE = "df -h"
printf "Gathering diskspace information with the $DISKSPACE command: \n\n"
$DISKSPACE
