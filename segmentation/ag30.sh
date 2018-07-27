#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes
#$ -pe mpich 8
#$ -l h='!puck3-gpu.cm.cluster'

#put qsub args


for i in 0 3 6
do
	echo 'agu30' $i
	./agu.sh ../CDS/english/Brent/30k/prepared_phoneme$i\.txt 'phoneme' ../CDS/english/Brent/30k/gold$i\.txt ../grammars/Colloc0_enFestival.lt
	./agu.sh ../CDS/english/Brent/30k/prepared_syllable$i\.txt 'syllable' ../CDS/english/Brent/30k/gold$i\.txt ../grammars/Colloc0syll_en.lt
	echo 'done agu30' $i
done
