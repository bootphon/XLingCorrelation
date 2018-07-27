#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#. /etc/profile.d/modules.sh

#module load python-anaconda boost

source activate wordseg
for line in $(find $1 -name '*prepared_phoneme*'); do

        number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
        /usr/bin/time ./dpseg.sh $line 'phoneme' $(dirname $line)/gold$number\.txt 2> time_phoneme.txt
done
for line in $(find $1 -name '*prepared_syllable*'); do

        number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
        /usr/bin/time ./dpseg.sh $line 'syllable' $(dirname $line)/gold$number\.txt 2> time_syllable.txt
done

