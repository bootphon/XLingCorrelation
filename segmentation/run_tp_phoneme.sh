#!/bin/bash
#$-S /bin/bash
#$ -cwd
#$ -j yes
#$ -l h=’puck1.cm.cluster|puck2.cm.cluster’
#. /etc/profile.d/modules.sh

#module load python-anaconda boost

#source activate wordseg
for line in $(find $1 -name '*prepared_phoneme*'); do

        number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
        echo $line $(dirname $line)/gold$number\.txt
        ./tp.sh $line 'phoneme' $(dirname $line)/gold$number\.txt relative forward
        ./tp.sh $line 'phoneme' $(dirname $line)/gold$number\.txt relative backward
        ./tp.sh $line 'phoneme' $(dirname $line)/gold$number\.txt absolute forward
        ./tp.sh $line 'phoneme' $(dirname $line)/gold$number\.txt absolute backward
done
