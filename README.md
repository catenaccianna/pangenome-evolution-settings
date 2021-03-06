# Pangenome Evolution Settings
Analysis tools used to set conditions of evolution in pangenomes. Evolution is conducted with a crossover operator modeled after DeBruijn graphs:

[![DOI](https://github.com/catenaccianna/pangenomes-for-evolutionary-computation.git)](https://github.com/catenaccianna/pangenomes-for-evolutionary-computation)

Evolutionary Computation is conducted through Version 2 of the Modular Agent-Based Evolver:

[![DOI](https://github.com/mercere99/MABE2.git)](https://github.com/mercere99/MABE2)

This repository contains sbatch scripts, settings files, and data for running MABE2 under the settings chosen to test the effect of this crossover operator on the
evolution of a population.

## Contents of this repository

- **SBATCH Scripts**: These are the scripts used to execute a trial of 30 replicants (using SLURM) on the remote HPCC server.
- **Settings Files**: These are the .mabe and .gen files that are used to specify the settings we are running each replicant under in MABE2.
- **Data**: CSV files contain all information we want to keep track of--condition, random seed, time step, number of unique genotypes in the population, and average, 
dominant, maximum, and minimum fitness.
- **CombineCsv Script**: This is the script used to combine all the data resulting from 30 replicants in once condition into a single CSV file.

#### Methods

Sbatch files were used to run trials in HPCC, using the .mabe settings files. Resulting CSV files were scp-ed from the remote HPCC server to my local computer, and 
the CombineCsv Script was run on these files to produce one CSV file for every condition tested. These CSV files were imported into RStudio to visualize the data.
