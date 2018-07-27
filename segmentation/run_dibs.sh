#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#. /etc/profile.d/modules.sh

#module load python-anaconda boost

#source activate wordseg
for line in $(find $1 -name '*prepared_phoneme*'); do
	
	number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
	echo $line $(dirname $line)/gold$number\.txt
	./dibs.sh $line 'phoneme' $(dirname $line)/gold$number\.txt
done
for line in $(find $1 -name '*prepared_syllable*'); do
        
	number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
	./dibs.sh $line 'syllable' $(dirname $line)/gold$number\.txt
done
