#!/usr/bin/env bash
# cleaning up selected lines from cha files in prep to generating a phono format
# Alex Cristia alecristia@gmail.com 2015-10-26
LC_CTYPE=C
#########VARIABLES
#Variables that have been passed by the user
SELFILE=$1
ORTHO=$2
TEST='test'
#########

echo "Cleaning $SELFILE"

#replacements to clean up CHAT style punctuation, etc. -- usually ok regardless
#of the corpus
unset LANG

# cat $SELFILE | rev | cut -d ' ' -f2- | rev > $SELFILE$TEST
# cat $SELFILE | sed 's/..[0123456789]*_[0123456789]*..//g' > $SELFILE$TEST

grep "*" < "$SELFILE" |

# cat $SELFILE |
sed 's/^....:.//g' |
# sed "s/\_/ /g" |
# sed '/^0(.*) .$/d' |
# sed  's/.*$//g' | #this code deletes bulletpoints (Û+numbers
# sed 's/^U.*^U//g' |
sed 's/..[0123456789][0123456789]*_[0123456789][0123456789]*..//g' |# replaces previous 4 lines - hopefully no encoding problem
# tr -d '\"' |
sed 's/_/ /g' |
tr -d '\^' | #used to be identical to previous line
tr -d '\/' |
sed 's/\+/ /g' |
tr -d '\.' |
tr -d '\?' |
tr -d '!' |
tr -d ';' |
tr -d '\<' |
tr -d '\>' |
tr -d ','  |
tr -d ':'  |
sed 's/&=[^ ]*//g' |
sed 's/&[^ ]*//g' |  #delete words beginning with & ##IMPORTANT CHOICE COULD HAVE CHOSEN TO NOT DELETE SUCH NEOLOGISMS/NONWORDS
sed 's/\[[^[]*\]//g' | #delete comments
# sed 's/([^(]*)//g' | #IMPORTANT CHOICE -- UNCOMMENT THIS LINE AND COMMENT OUT THE NEXT TO DELETE MATERIAL NOTED AS NOT PRONOUNCED
sed 's/(//g' | sed 's/)//g' | #IMPORTANT CHOICE -- UNCOMMENT THIS LINE AND COMMENT OUT THE PRECEDING TO REMOVE PARENTHESES TAGGING UNPRONOUNCED MATERIAL
sed 's/xxx//g' |
sed 's/www//g' |
sed 's/XXX//g' |
sed 's/yyy//g' |
sed 's/0*//g' |
sed 's/[^ ]*@s:[^ ]*//g' | #delete words tagged as being a switch into another language
#sed 's/[^ ]*@o//g' | #delete words tagged as onomatopeic
sed 's/@[^ ]*//g' | #delete tags beginning with @ IMPORTANT CHOICE, COULD HAVE CHOSEN TO DELETE FAMILIAR/ONOMAT WORDS
sed "s/\' / /g"  |
tr -s ' ' |
sed 's/ $//g' |
sed 's/^ //g' |
sed 's/^[ ]*//g' |
sed 's/ $//g' |
sed '/^$/d' |
sed '/^ $/d' |
sed 's/\^//g' |
awk '{gsub("\"",""); print}' > $ORTHO



#This is to process all the "junk" that were generated when making the
#changes from included to ortho.  For e.g., the cleaning process
#generated double spaces between 2 words (while not present in
#included)

sed -i -e 's/  $//g' $ORTHO
sed -i -e 's/  / /g' $ORTHO
sed -i -e 's/  / /g' $ORTHO
sed -i -e 's/^ //g' $ORTHO
sed -i -e 's/ $//g' $ORTHO
sed -i -e '/^$/d' $ORTHO
# sed -i -e '/\t/d' $ORTHO