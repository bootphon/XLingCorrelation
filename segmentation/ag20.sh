#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#$ -l h='!puck3-gpu.cm.cluster'

#put qsub args


for i in 0 2 4 6 8
do
	echo 'agu20' $i
	./agu.sh ../CDS/english/Brent/20k/prepared_phoneme$i\.txt 'phoneme' ../CDS/english/Brent/20k/gold$i\.txt ../grammars/Colloc0_enFestival.lt
	./agu.sh ../CDS/english/Brent/20k/prepared_syllable$i\.txt 'syllable' ../CDS/english/Brent/20k/gold$i\.txt ../grammars/Colloc0syll_en.lt
	echo 'done agu20' $i
done
