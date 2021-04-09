# TwinProtein


## How to run the code?

The following command allocates 8 executors to worker nodes and 1 executor to manager, with 2 cpus per task and a limit of 2 maximum gaps allowed in the permutation of protein sequence.

~~~
spark-submit --master spark://crill:28959 --total-executor-cores 8
    --executor-cores 2 code/prscore.py protein-1.txt
    db-small.txt 2
~~~


## Aim

We are provided with a protein sequence (P) of amino acids in a text file. The file contains a 42 character long string consisting of letters like M, R, K... which represents different amino acids.

3 databases of proteins db-tiny.txt, db-small.txt, db-large.txt which contains 5, 66, and 100 different types of already known proteins respectively.

The task is to find a close match of the P in these databases. We calculate a certain score based on defined parameters on matching sequences and take the top 25 results from all the permutations possible of the P.

What makes this problem complex? The possible permutations of P which can be introduced with the number of gaps (‘-’) and spaces (‘ ’) is huge. For each entry in the database there are enormous possible permutations of P. Comparing each permutation with the entries in database is time consuming. Thus, we try to parallelize the implementation of the calculating the score variants with the help of PySpark and Crill cluster.

## Steps

Step 1: Read the database file with spark context object and repartiton based on the size of db file.

Step 2: Pass the (P , DB, max_gaps) through flatMap to GetScoresWithVariants() which returns tuple like (scorej, (P , DB))

Step 3: Sort based on the key that is the score value, and take the top N ele- ments which we can now easily write in a txt file.














