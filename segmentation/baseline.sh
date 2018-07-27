#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -l h='!puck3-gpu.cm.cluster'
#. /etc/profile.d/modules.sh

#module load python-anaconda boost

#source activate wordseg

PATH_CDS=$(dirname $1)
PATH_RES=$(echo $PATH_CDS | sed -e "s/CDS/Results/g")
number=$(echo $(basename $1) | egrep -o '[[:digit:]]' | head -n1)
cat $1 | wordseg-baseline -P $4 > $PATH_RES/baseline$4/$2/segmented$number\.txt
echo 'segment'
cat $PATH_RES/baseline$4/$2/segmented$number\.txt | wordseg-eval $3 > $PATH_RES/baseline$4/$2/eval$number\.txt
echo 'eval'
