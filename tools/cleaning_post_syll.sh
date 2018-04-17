#!/bin/bash
cp $1 $2
sed -i -e 's/ /;eword/g' $2
sed -i -e 's/[^ː-]/ &/g' $2
sed -i -e 's/^.//g' $2
sed -i -e 's/; e s y l l/;esyll/g' $2
sed -i -e 's/; e w o r d/;eword/g' $2
sed -i -e 's/  / /g' $2
