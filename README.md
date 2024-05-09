# Position-Specific Scoring Matrix (PSSM)

This Python script calculates a Position-Specific Scoring Matrix (PSSM) for a set of aligned DNA sequences. Additionally, it allows for the generation of random sequences and calculates the probability of a new sequence joining the alignment based on the PSSM

# requirement

Python 3.x
NumPy library (for matrix operations)

# Input Options

1-Read from file: If chosen, the script will prompt you to enter the filename containing the DNA sequences. It expects the file format to have one sequence per line.

2-Generate random sequences: If chosen, the script will ask for the number of sequences (t) and the length of each sequence (n) to be generated randomly.

# Output

The script displays the multiple aligned DNA sequences.
It then calculates and prints the PSSM matrix, showing the logarithmic frequency of each nucleotide at each position in the alignment.
Finally, it prompts for a new sequence of the same length as the alignment and calculates the probability of this new sequence joining the alignment based on the PSSM.

# Functionality

## PSSM(sequences)
1 -Computes the Position-Specific Scoring Matrix (PSSM) for a given set of aligned DNA sequences.

2- Returns a list of dictionaries representing the frequencies of nucleotides at each position.

## read_file(name)

1 -Reads DNA sequences from a file specified by name.

2 - Returns a list of DNA sequences.

## generate_random(t, n)

1 - Generates t random DNA sequences, each of length n.

2 - Returns a list of randomly generated DNA sequences.

## calcProbability(frequencies)
1 - Prompts for a new sequence of the same length as the alignment.

2 - Calculates and prints the probability of the new sequence joining the alignment based on the PSSM.

## main()

The main function orchestrating the program execution.
Provides user interface for choosing input method and displaying results.

