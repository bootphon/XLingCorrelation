#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes


#. /etc/profile.d/modules.sh

#module load python-anaconda boost

#source activate wordseg

PATH_CDS=$(dirname $1)
PATH_RES=$(echo $PATH_CDS | sed -e "s/CDS/Results/g")
number=$(echo $(basename $1) | egrep -o '[[:digit:]]' | head -n1)
wordseg-dibs -t phrasal -o $PATH_RES/dibs/$2/segmented$number\.txt $1 $PATH_CDS/training_dibs$number\.txt
#echo 'segment'

cat $PATH_RES/dibs/$2/segmented$number\.txt | wordseg-eval $3 > $PATH_RES/dibs/$2/eval$number\.txt
#echo 'eval'
