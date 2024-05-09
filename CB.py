import random
import math
import numpy as np

def PSSM(sequences):
    counts = []
    for i in range(len(sequences[0])):
            column = [seq[i] for seq in sequences]
            count_A = column.count('A')
            count_C = column.count('C')
            count_G = column.count('G')
            count_T = column.count('T')
            
            counts.append({'A': count_A, 'C': count_C, 'G': count_G, 'T': count_T})
    frequencies = []   
    for count_dict in counts:
        freq_dict = {}
        total = sum(count_dict.values())
        for base, count in count_dict.items():
            freq_dict[base] = count / total
        frequencies.append(freq_dict)

    countA = 0.0
    countG = 0.0
    countC = 0.0
    countT = 0.0
    size = len(sequences[0]) * len(sequences)

    for i in range(len(sequences[0])):
        for seq in sequences:
            if seq[i] == 'A':
                countA += 1
            elif seq[i] == 'G':
                countG += 1
            elif seq[i] == 'C':
                countC += 1
            elif seq[i] == 'T':  
                countT += 1
                    
    countA = countA / size
    countG = countG / size
    countC = countC / size 
    countT = countT / size 


    for freq_dict in frequencies:
        for base, freq in freq_dict.items():
            if base == 'A' and countA != 0:
                freq_dict[base] = freq / countA
            elif base == 'C' and countC != 0:
                freq_dict[base] = freq / countC
            elif base == 'G' and countG != 0:
                freq_dict[base] = freq / countG
            elif base == 'T' and countT != 0:
                freq_dict[base] = freq / countT
                

    for freq_dict in frequencies:
        for base, freq in freq_dict.items():
            if freq > 0:
                freq_dict[base] = math.log(freq, 2)

    print("APPLYING")
    print("PSSM MATRIX:")
    print("    A            C            G            T")
    for freq_dict in frequencies:
        for base,freq in freq_dict.items():
            if(freq<0):
                print(f"   {freq:.2f}    ", end=" ")
            else:
                print(f"    {freq:.2f}    ", end=" ")
        print()
    return frequencies


def read_file(name):
    try:
        with open(name) as file:
            seq = file.readlines()[1:]
            return [sequence.strip() for sequence in seq]
    except FileNotFoundError:
        return 

def generate_random(t, n):
    nucleotides = ['A', 'C', 'G', 'T']
    seq = []
    for _ in range(t):
        sequence = ''.join(random.choice(nucleotides) for _ in range(n))
        seq.append(sequence)
    return seq

def print_sequence(seq):
    print("Multiple Aligned DNA Sequences:")
    for i, sequence in enumerate(seq, start=1):
        print(f"sequence {i} : {sequence}")

def calcProbability(frequencies):
    test=input(f"Enter a new sequence of length {len(frequencies)}")
    total=0
    for i in range(len(test)):
        total+=frequencies[i][test[i]]
    print(f"probability of new sequence joining the alignment:{2**total}")
    
def main():   
   print("Position-Specific Scoring Matrix (PSSM)")
   print("Choose input method:")
   print("1. Read from file")
   print("2. Generate random Sequence")
   choice = input("Enter your choice: ")

   if choice == '1':
       name=input("enter filename:")
       print("Reading input from file ...")
       seq = read_file(name)
       if not seq:
           print("wrong file name or file doesn't exist")
           return
       print(f"Found {len(seq)} sequences of length {len(seq[0])} \n")

   elif choice == '2':
       print("Generating random sequences ... \n")
       t = int(input("Enter the number of sequences (t): "))
       n = int(input("Enter the length of each sequence (n): "))
       seq = generate_random(t, n)
   else:
       print("Invalid choice")
       return
   
   print("multiple aligned sequences")
   
   for i in range(len(seq)):
       print(f"sequence {i+1} : {seq[i]}")
       
   frequencies=PSSM(seq)
   calcProbability(frequencies)

main()