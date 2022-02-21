#!/bin/bash
# use back ticks " ` ` " to execute shell command
echo `uname -a`
# save command in a variable
lines=`ls| wc -l`
echo Number of lines is $lines
