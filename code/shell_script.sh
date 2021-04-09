#!/bin/bash
#SBATCH -J  proparscore
#SBATCH -t 01:00:00
#SBATCH -N 5
#SBATCH -p cosc6339
#SBATCH --cpus-per-task 2


module load spark/2.3.4
crill-spark-submit -a 2 prscore.py protein-1.txt dbase-small.txt 2
exit
