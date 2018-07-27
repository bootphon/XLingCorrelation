#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -l h='!puck3-gpu.cm.cluster'

#module load python-anaconda boost

#source activate wordseg
for line in $(find $1 -name '*prepared_phoneme*'); do
	
	number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
	echo $line $(dirname $line)/gold$number\.txt
	./baseline.sh $line 'phoneme' $(dirname $line)/gold$number\.txt 1
	./baseline.sh $line 'phoneme' $(dirname $line)/gold$number\.txt 0
done
for line in $(find $1 -name '*prepared_syllable*'); do
        
	number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
	./baseline.sh $line 'syllable' $(dirname $line)/gold$number\.txt 1
	./baseline.sh $line 'syllable' $(dirname $line)/gold$number\.txt 0
done
