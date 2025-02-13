# Report for Assignment 0
### By Zeyad Aljaali

## Description
To compare the strings we used the naive algorithm. For the up to one mismatch we first used the pigeone principle approach, the we used the naive approach to check the other half.
As for managing the RAM, we read the file containing the text in chunks from the .gz using pysam and decoding it using io (here I used the chunks being the chromosomes to make the implementaion easier, but this could be chosen to fit a specific space in RAM). We then used the time command line tool to find the time and peak memory usage.

## Part I & II
The file exact.py should output the result for exact matches, and offby1.py should output the results for up to one mismatch.
Note, we need to manipulate the filename for each genome in the script and run it.  Also the start and end value are relative for the chromosome.

## Part III
### Results for exact matches
#### GRCh:  3 exact matches
CM000665.2 HOMO SAPIENS CHROMOSOME 3, GRCH38 REFERENCE PRIMARY ASSEMBLY, start = 88629832, end = 88630142

CM000669.2 HOMO SAPIENS CHROMOSOME 7, GRCH38 REFERENCE PRIMARY ASSEMBLY, start = 39808489, end = 39808799

CM000679.2 HOMO SAPIENS CHROMOSOME 17, GRCH38 REFERENCE PRIMARY ASSEMBLY, start = 18689763, end = 18690073

#### T2T: 2 exact matches
CP068276.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 2, start = 186833277, end = 186833587

CP068271.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 7, start = 39966041, end = 39966351


### Results for up to one mismatches
Note, kind represents the kind of mismatch we have.
rep = replacement, insr = insertion, del = deletion, exact = exact match

#### GRCh: 16 up to one mismatch (this includes exact matches) 
CM000663.2 HOMO SAPIENS CHROMOSOME 1, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=85940122, kind=rep

CM000663.2 HOMO SAPIENS CHROMOSOME 1, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=144846234, kind=rep

CM000665.2 HOMO SAPIENS CHROMOSOME 3, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=69313857, kind=rep

CM000665.2 HOMO SAPIENS CHROMOSOME 3, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=88629832, kind=exact

CM000666.2 HOMO SAPIENS CHROMOSOME 4, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=132898458, kind=rep

CM000667.2 HOMO SAPIENS CHROMOSOME 5, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=125028156, kind=rep

CM000669.2 HOMO SAPIENS CHROMOSOME 7, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=39808489, kind=exact

CM000670.2 HOMO SAPIENS CHROMOSOME 8, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=100790760, kind=rep

CM000674.2 HOMO SAPIENS CHROMOSOME 12, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=62838639, kind=rep

CM000675.2 HOMO SAPIENS CHROMOSOME 13, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=63082060, kind=rep

CM000676.2 HOMO SAPIENS CHROMOSOME 14, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=34836097, kind=rep

CM000677.2 HOMO SAPIENS CHROMOSOME 15, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=53225105, kind=rep

CM000679.2 HOMO SAPIENS CHROMOSOME 17, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=18689763, kind=exact

CM000679.2 HOMO SAPIENS CHROMOSOME 17, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=19593503, kind=rep

CM000683.2 HOMO SAPIENS CHROMOSOME 21, GRCH38 REFERENCE PRIMARY ASSEMBLY, loc=26516833, kind=rep

KI270778.1 HOMO SAPIENS CHROMOSOME 3 GENOMIC CONTIG, GRCH38 REFERENCE ASSEMBLY ALTERNATE LOCUS GROUP ALT_REF_LOCI_1, loc=54847, kind=rep

#### T2T: 20 up to one mismatch (this includes exact matches)
CP068277.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 1, loc=143946938, kind=rep

CP068277.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 1, loc=190858894, kind=rep

CP068276.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 2, loc=186833277, kind=exact

CP068275.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 3, loc=69350794, kind=rep

CP068274.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 4, loc=136221657, kind=rep

CP068273.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 5, loc=126911808, kind=rep

CP068272.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 6, loc=51234801, kind=rep

CP068272.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 6, loc=68212687, kind=rep

CP068271.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 7, loc=39966041, kind=exact

CP068271.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 7, loc=49189460, kind=rep

CP068270.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 8, loc=101916771, kind=rep

CP068267.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 11, loc=86916177, kind=rep

CP068266.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 12, loc=62817411, kind=rep

CP068266.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 12, loc=79100751, kind=rep

CP068265.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 13, loc=66839102, kind=insr

CP068264.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 14, loc=17947515, kind=rep

CP068261.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 17, loc=2142369, kind=rep

CP068261.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 17, loc=19541649, kind=rep

CP068260.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 18, loc=66026304, kind=rep

CP068257.2 HOMO SAPIENS ISOLATE CHM13 CHROMOSOME 21, loc=24874951, kind=rep


## Part IV

### Results for exact matches
#### GRCh:  time: 6m34.53s, peak memory: 289.17MB
#### T2T:   time: 6m57.44s,  peak memory: 310.31MB

### Results for up to one mismatches
#### GRCh:  time: 11m37.64s, peak memory: 267.81MB
#### T2T:   time: 10m23.53s, peak memory: 286.36MB


## Part V
### Reading compressed files is implemented using pysam and io
### Handling sequences bigger than the RAM is implemented
In the code we segment by chromosome, but we could easily change the segmentation to be of a fixed size for memory.

