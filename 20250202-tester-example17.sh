#!/bin/bash

for((i=0; i<=7; i++))
do
    curl 192.168.1.22:8080/?=$i
    echo $i
    sleep 0.5
done
for((i=7; i>=0; i--))
do
    curl 192.168.1.22:8080/?=$i
    echo $i
    sleep 0.5
done

