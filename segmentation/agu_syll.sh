#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
. /etc/profile.d/modules.sh

module load python-anaconda boost

source activate wordseg
# prepare the input for segmentation and generate the gold text
#cat /scratch2/gbaudet/tags.txt | wordseg-prep -vv -u syllable --gold /scratch2/gbaudet/gold.txt > /scratch2/gbaudet/prepared_syll.txt
#AG has a similar call but additional files can be provided
#GRAMMAR=test/data/ag/Colloc0_enFestival.lt
GRAMMAR=Colloc0syll_en.lt
CATEGORY=Colloc0
cat prepared_syll.txt | wordseg-ag  $GRAMMAR $CATEGORY --njobs 8 --verbose > AG_syll/segmented.ag_syll.txt
cat AG_syll/segmented.ag_syll.txt | wordseg-eval gold.txt > AG_syll/eval.ag_syll.txt
