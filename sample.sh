#!/bin/bash

cat COVID-19.csv | while read line
do
	col1=`echo ${line} | cut -d ',' -f 8`
	
	${col1} > out.csv
	
done < COVID-19.csv