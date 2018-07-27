#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#$ -l h='!puck3-gpu.cm.cluster'

#. /etc/profile.d/modules.sh

#module load python-anaconda boost

#source activate wordseg
for line in $(find $1 -name '*prepared_phoneme*'); do

        number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
        ./agu.sh $line 'phoneme' $(dirname $line)/gold$number\.txt $2
done
for line in $(find $1 -name '*prepared_syllable*'); do

        number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
        ./agu.sh $line 'syllable' $(dirname $line)/gold$number\.txt $3
done
