# /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
. /etc/profile.d/modules.sh

module load python-anaconda boost

source activate wordseg

# prepare the input for segmentation and generate the gold tet
cat $1 | wordseg-prep -vv -u syllable --gold $(dirname $1)/gold$2\.txt > $(dirname $1)/prepared_syllable$2\.txt

