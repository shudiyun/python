#!/bin/bash

count=1

while [ $count -lt 16 ]
do
  echo $count
  python scikit.py img/ $count
  (( count++ ))
done
