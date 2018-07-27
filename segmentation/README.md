## Tools

### count_phono.py

Counts and sorts the phones appearing in a phonologized corpus

### to_freq.sh

builds freqtop for each segmented file

## Global segmentation architecture

run\_all.sh creates the right architecture to store the results, prepares the tags (in phones or syllables) and the summary for dibs, and calls run\_algo.sh for each algo. 
In turn, each run\_algo.sh calls algo.sh with different arguments - most of the time, different units, but sometimes other parameters (example : TP, AGu)

Each script can be run separately.
The tag files have to be in CDS/language/corpus\_name/  ; the architecture creation will be done in Results/language/corpus\_name (you need an existing Results/language/ directory) 

Output is segmented corpus by different algos+corresponding evaluation

ag[number].sh is what was used to segment selected portion of the Brent corpus


### run_all.sh

+ $1 : path/to/dir/containing/tags/
+ $2 : path/to/phone_grammar.lt
+ $3 : path/to/syllable_grammar.lt

### create\_archi.sh
+ $1 : path/to/dir/to/create/
RES : the right architecture for following scripts to store their results


### prepare\_phoneme.sh / prepare\_syllable.sh
+ $1 : PATH/TO/tags.txt
+ $2 : number of sub if sub
RES: PATH/TO/gold\*.txt
     PATH/TO/prepared_unit\*.txt

### prepare\_all.sh
Calls both prepare\_syllable and prepare\_phoneme on all tags in the given directory
+ $1 : PATH/TO/ : directory in which to find all tags\*.txt
RES: PATH/TO/gold PATH/TO/prepared\*

### run\_baseline.sh
Calls ./baseline.sh path/to/prepared\_unit\*.txt unit path/to/gold\*.txt
for all prepared in $1 and for unit in phoneme, syllable

/!\ CAN ONLY BE RUN FROM THIS VERY DIRECTORY /!\ otherwise, change './baseline.sh'

+ $1 : directory in which to find all prepared\*.txt to segment

### baseline.sh

+ $1 : path/to/prepared\_unit\*.txt
+ $2 : unit
+ $3 : path/to/gold\*.txt

calls baseline on tags.txt, outputs the segmentation in the right place and the evaluation compared to the gold

### run\_dpseg.sh

+ $1 : directory in which to find all prepared\*.txt to segment

### dpseg.sh

+ $1 : path/to/prepared\_unit\*.txt
+ $2 : unit
+ $3 : path/to/gold\*.txt

calls baseline on tags.txt, outputs the segmentation in the right place and the evaluation compared to the gold

### run\_agu.sh

+ $1 : directory in which to find all prepared\_unit\*.txt
+ $2 : phoneme grammar
+ $3 : syllable grammar

### agu.sh

+ $1 : path/to/prepared\_unit\*.txt
+ $2 : unit
+ $3 : path/to/gold.txt
+ $4 : grammar, in accordance with unit

### run\_puddle.sh

### puddle.sh

### run\_dibs.sh

### dibs.sh

### run\_tp.sh

### tp.sh

# PATHS PROBABLY HAVE TO BE CHANGED
