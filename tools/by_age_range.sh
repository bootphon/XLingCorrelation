#!/bin/bash

mkdir $1/by_age_range/
mkdir $1/by_age_range/0/
mkdir $1/by_age_range/1/
mkdir $1/by_age_range/2/
mkdir $1/by_age_range/3/

for line in $(find $1 -name '0[0-9][0-9][0-9][0-9]*.cha'); do
# good only for French/Lyon, add 0 at beginning otherwise
	cat $line >> $1/by_age_range/0/concatenated.txt
done	

for line in $(find $1 -name '1[0-9][0-9][0-9][0-9]*.cha'); do
# good only for French/Lyon, add 0 at beginning otherwise
        cat $line >> $1/by_age_range/1/concatenated.txt
done

for line in $(find $1 -name '2[0-9][0-9][0-9][0-9]*.cha'); do
# good only for French/Lyon, add 0 at beginning otherwise
        cat $line >> $1/by_age_range/2/concatenated.txt
done

for line in $(find $1 -name '3[0-9][0-9][0-9][0-9]*.cha'); do
# good only for French/Lyon, add 0 at beginning otherwise
        cat $line >> $1/by_age_range/3/concatenated.txt
done

rm -r by_age_range/by_age_range
