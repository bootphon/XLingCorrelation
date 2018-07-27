touch $2
#remove first 0 for French/Lyon
for line in $(find $1 -name '*0[0-3][0-9][0-9][0-9][0-9]*.cha'); do
     cat $line >> $2
done
