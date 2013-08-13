#! /usr/bin/env bash

#simple function and for loop in bash

function shfunc(){
    printf "Hello function\n"
}

for (( i=0; i<5; i++ ))
do
    shfunc
done

