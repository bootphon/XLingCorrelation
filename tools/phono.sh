#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -l h='!puck3-gpu.cm.cluster'

echo 'start'
#module load python-anaconda boost
module load espeak
cat $1 | phonemize -l $2 > $3
echo 'end'
