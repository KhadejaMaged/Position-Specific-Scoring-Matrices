Position-Specific Scoring Matrix (PSSM)
This Python script calculates a Position-Specific Scoring Matrix (PSSM) for a set of aligned DNA sequences. Additionally, it allows for the generation of random sequences and calculates the probability of a new sequence joining the alignment based on the PSSM.

Requirements
Python 3.x
NumPy library (for matrix operations)
Usage
Running the script
Clone or download the script (pssm.py) to your local machine.
Open a terminal or command prompt.
Navigate to the directory where pssm.py is located.
Run the script by executing python pssm.py.
Input Options
Read from file: If chosen, the script will prompt you to enter the filename containing the DNA sequences. It expects the file format to have one sequence per line.
Generate random sequences: If chosen, the script will ask for the number of sequences (t) and the length of each sequence (n) to be generated randomly.
Output
The script displays the multiple aligned DNA sequences.
It then calculates and prints the PSSM matrix, showing the logarithmic frequency of each nucleotide at each position in the alignment.
Finally, it prompts for a new sequence of the same length as the alignment and calculates the probability of this new sequence joining the alignment based on the PSSM.
Functionality
PSSM(sequences)
Computes the Position-Specific Scoring Matrix (PSSM) for a given set of aligned DNA sequences.
Returns a list of dictionaries representing the frequencies of nucleotides at each position.
read_file(name)
Reads DNA sequences from a file specified by name.
Returns a list of DNA sequences.
generate_random(t, n)
Generates t random DNA sequences, each of length n.
Returns a list of randomly generated DNA sequences.
calcProbability(frequencies)
Prompts for a new sequence of the same length as the alignment.
Calculates and prints the probability of the new sequence joining the alignment based on the PSSM.
main()
The main function orchestrating the program execution.
Provides user interface for choosing input method and displaying results.
