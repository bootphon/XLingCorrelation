#!/bin/bash
#$ -S /bin/bash
#$ -wd /scratch2/gbaudet/scripts/
#$ -j yes 
#$ -l h='!puck3-gpu.cm.cluster'


###$ -pe mpich 8


# in $1 : directory of CDS to use, containing tags.txt
# in $2, $3 : grammars phoneme / syll
NAME=$(basename $1)
echo $NAME
# 1. create architecture
# create_archi.sh ($1 with /CDS/ replaced by /Results/)
PATH_CDS=$1 
PATH_RES=$(echo $PATH_CDS | sed -e "s/CDS/Results/g")
./create_archi.sh $PATH_RES

# 2. prepare data
./prepare_all.sh $1
./training_dibs.sh $1

# 3. run !
echo 'baseline'
./run_baseline.sh $1
#echo 'dpseg'
#./run_dpseg.sh $1
echo 'dibs'
./run_dibs.sh $1
echo 'puddle'
./run_puddle.sh $1
echo 'tp'
./run_tp.sh $1

#echo 'agu'
#./run_agu.sh $1 $2 $3
