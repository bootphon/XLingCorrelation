#!/bin/bash


mkdir $1/by_child/
cd $1
for d in */ ; do
	echo "$d"
	mkdir by_child/$d/
	/Users/gladysbaudet/Desktop/PFE/scripts/group_cha.sh $d ./by_child/$d/concatenated.txt
done
rm -r by_child/by_child
