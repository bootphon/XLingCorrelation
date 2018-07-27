#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes

. /etc/profile.d/modules.sh

module load python-anaconda boost

source activate wordseg

for line in $(find $1 -name '*tags*'); do
     number=$(echo $(basename $line) | egrep -o '[[:digit:]]' | head -n1)
     head -200 $line > $(dirname $line)/training_dibs$number\.txt
     sed -i '/^\s*$/d' $(dirname $line)/training_dibs$number\.txt
done
