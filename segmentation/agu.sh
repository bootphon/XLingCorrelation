#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#$ -l h='!puck3-gpu.cm.cluster'

# Following 3 lines already in .bashrc / uncomment if not
#. /etc/profile.d/modules.sh
#module load python-anaconda boost
#source activate wordseg

#GRAMMAR=test/data/ag/Colloc0_enFestival.lt

# $1 : path/to/prepared.txt
# $2 : unit
# $3 : path/to/gold.txt
# $4 : grammar (according to prepared) 
#GRAMMAR=Colloc0_enFestival.lt

GRAMMAR=$4
CATEGORY=Colloc0
PATH_CDS=$(dirname $1)
PATH_RES=$(echo $PATH_CDS | sed -e "s/CDS/Results/g") # works only with the right architecture (CDS and Results have same sub-tree) 
number=$(echo $(basename $1) | egrep -o '[[:digit:]]' | head -n1) # recover number of sample if sample (else '') 
cat $1 | wordseg-ag $GRAMMAR $CATEGORY --njobs 8 -vv > $PATH_RES/ag/$2/segmented$number\.txt
cat $PATH_RES/ag/$2/segmented$number\.txt | wordseg-eval $3 > $PATH_RES/ag/$2/eval$number\.txt
