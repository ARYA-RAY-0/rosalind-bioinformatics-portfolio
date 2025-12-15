#!/usr/bin/env python3
"""
Rosalind Problem: REVC (Reverse Complement)
Problem ID: REVC
URL: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.
Return: Its reverse complement sc.
"""

def reverse_complement(dna_string: str) -> str:
    """
    Returns the reverse complement of a DNA sequence.

    Steps:
    1. Reverse the string.
    2. Replace each base with its complement (A<->T, C<->G).

    Args:
        dna_string (str): Input DNA sequence (A, C, G, T only).

    Returns:
        str: The reverse complement sequence.
    """
    # Step 1: Define the complement mapping
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    # Step 2: Reverse the string and build the complement
    reversed_string = dna_string[::-1]  # Slicing trick to reverse
    complement_list = [complement_map[base] for base in reversed_string]

    # Step 3: Join the list back into a string
    return ''.join(complement_list)

def main():
    # Read the input DNA string (paste your dataset here into s)
    # Example: s = "AAAACCCGGT"
    s = "TCGTACAGGCCTTCGGGGAATTGTCCAGCGTTAGAACTCCCCCGTGCCACGAGCGGCGATGTATCGTAGTACGCCTTCCGTAGATCGTGAGTTGGTATGAATCTGACTATTAGGGGCGTTCTCAAGTACTTTCTGATGGGTGTAACCAAATATTCAGCATACCGGTTGCTCGACCCGACTCCGTGCTTCGTGCTGTCCGGCGAAGCGTTACCCGGAAGGACACGAGACGGAGGCTAGCATAAATGAGGTACAGTAAGTCGCGCTTGCGAACTTGAATTTCGCTGGCAACCGACGGTAAATGTGAATTGATCGAGACTTGGGTCTAGACATAACGCGCACCGCAATCGTCGTGTTTGTCCTTCTCCTGTCGATTCCAAGTATGTCCTATTGTCTGCAATGTCGAGGTGGTCATAGTAAGACCAATAAGCCGGTTACTGGAATTGTGTTGTCGGAGGGCAATGCATCGTTAGTTACATCTTAACACAAATGTTTTACGTATTTTACGGACGCACCAGATCTATCAAATGCAGCCCGGGCTCAGATTAAGTATAAGCTGGGAGAAACCGTAACACCCAACCACCTGGCCAACACGGGCAAGACACCTATCGATCTCGACGATCTGCCCATTCTTCCGGTGATTATCAGAGTCGAGGCATAGTCAGTACGTTCCACATGGGCTAATTTCCGTTCCATGATATTGTCCGAGCACCCTAAGGTCGCACTGACGTGAAAAGTCTGTTGTCGTATAATGTCGGAATTTATAGAGAACCCCCAGTCTGCGAACACGCTTGTGAGCGAGGCTGATGCTGGGTC"  # REPLACE THIS WITH YOUR DATASET

    # Compute the reverse complement
    result = reverse_complement(s)

    # Print the result
    print(result)

    # Optional: Save output
    # with open('revc_output.txt', 'w') as f:
    #     f.write(result)

if __name__ == "__main__":
    main()