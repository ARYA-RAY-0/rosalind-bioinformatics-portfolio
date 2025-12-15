# Read the input string (you'll paste Rosalind's dataset here)
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Count the nucleotides
a_count = s.count('A')
c_count = s.count('C')
g_count = s.count('G')
t_count = s.count('T')

# Print the result in the required format
print(f"{a_count} {c_count} {g_count} {t_count}")