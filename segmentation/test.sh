#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j yes

if [ -z ${1+x} ]; then echo '1 is unset'; else echo $1; fi

