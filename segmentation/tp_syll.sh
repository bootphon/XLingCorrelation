#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
. /etc/profile.d/modules.sh

module load python-anaconda boost

source activate wordseg

cat prepared_syll.txt | wordseg-tp -p forward -t relative > segmented.tp.frel.txt
cat prepared_syll.txt | wordseg-tp -p forward -t absolute > segmented.tp.fabs.txt
cat prepared_syll.txt | wordseg-tp -p backward -t relative > segmented.tp.brel.txt
cat prepared_syll.txt | wordseg-tp -p backward -t absolute > segmented.tp.babs.txt


