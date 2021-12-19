#!/bin/bash

# $2 = password
# $1 = ip address

snmpwalk -v2c -c $2 $1 > output.txt

IN=$(grep 3.6.1.2.1.2.2.1.10.1 "./output.txt")
OUT=$(grep 3.6.1.2.1.2.2.1.16.1 "./output.txt")
SPEED=$(grep 3.6.1.2.1.2.2.1.5.1 "./output.txt")

VAR="${IN} ${OUT} ${SPEED}"

echo $VAR > ./output.txt