
#!/usr/bin/env bash
# cleaning up selected lines from cha files in prep to generating a phono format
# Alex Cristia alecristia@gmail.com 2015-10-26

#########VARIABLES
#Variables that have been passed by the user
ORTHO=$1
#########

echo "Extra cleaning $ORTHO"

mv $ORTHO tmp.tmp

#********** A T T E N T I O N ***************
# check that the next set of replacements for unusual spellings is
# adapted to your purposes
    sed 's/whaddaya/what do you/g' < tmp.tmp |
    sed 's/whadda/what do/g' |
    sed 's/whatcha/what you/g' |
    sed 's/haveto/have to/g' |
    sed 's/hasto/has to/g' |
    sed 's/outof/out of/g' |
    sed 's/lotsof/lots of/g' |
    sed 's/lotta/lots of/g' |
    sed 's/alotof/a lot of/g' |
    sed "s/wha\'s/what's/g" |
    sed "s/this\'s/this is/g" |
    sed 's/chyou/ you/g' |
    sed "s/dont you/don\'t you/g" |
    sed 's/wanta/wanna/g'  |
    sed "s/ whats / what\'s /g" |
    sed "s/'re/ are/g" |
    sed "s/klenex/kleenex/g" |
    sed 's/yogourt/yogurt/g' |
    sed 's/hmm+/hum/g' |
	  sed 's/mhm+/hum/g' |
    sed 's/ooo+h/oh/g' |
    sed 's/ohh/oh/g' |
    sed 's/ ha / have to /g' |
    sed 's/thau/thank you/g' |
    # tr -d '\t' |
    # tr -s ' ' |
    # sed '/^$/d'  |
    sed 's/ $//g' |
    sed 's/^ //g'  > "$ORTHO"

rm tmp.tmp
