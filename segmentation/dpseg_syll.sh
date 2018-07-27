#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes

. /etc/profile.d/modules.sh

module load python-anaconda boost

source activate wordseg
# prepare the input for segmentation and generate the gold text
cat /scratch2/gbaudet/tags.txt | wordseg-prep -vv -u syllable --gold /scratch2/gbaudet/gold.txt > /scratch2/gbaudet/prepared_dp_syllable.txt
#AG has a similar call but additional files can be provided
#GRAMMAR=test/data/ag/Colloc0_enFestival.lt
GRAMMAR=Colloc0syll_en.lt
CATEGORY=Colloc0
cat prepared_dp_syllable.txt | wordseg-dpseg > segmented.dpseg_syllable.txt
cat segmented.dpseg_syllable.txt | wordseg-eval gold.txt > eval.dpseg_syllable.txt
