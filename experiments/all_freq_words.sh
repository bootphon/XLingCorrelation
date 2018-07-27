#!/bin/bash

for line in $(find $1 -name '*segmented*'); do
	python ./write_freq_words.py $line $2 $3 $(pwd $line)/freq_words.txt
done
