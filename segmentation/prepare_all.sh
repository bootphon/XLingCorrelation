#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#. /etc/profile.d/modules.sh

#module load python-anaconda boost

source activate wordseg

for line in $(find $1 -name '*tags*'); do
     number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1) 
     ./prepare_phoneme.sh $line $number
     ./prepare_syllable.sh $line $number
done
