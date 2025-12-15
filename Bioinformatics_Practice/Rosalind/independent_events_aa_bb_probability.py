# ============================================================
# ROSALIND PROBLEM: INDEPENDENT EVENTS - Probability of Aa Bb offspring
# INPUT: k (generation), N (minimum Aa Bb offspring)
# OUTPUT: Probability at least N Aa Bb organisms in k-th generation
# ============================================================

from math import comb

# Paste your input here
k = 6  # generation
N = 18  # minimum Aa Bb offspring

# ------------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE
# ------------------------------------------------------------

# Number of organisms in k-th generation
num_offspring = 2 ** k

# Probability of Aa Bb for a single offspring (independent)
# Mendel's second law: Aa x Aa -> 1/4 AA, 1/2 Aa, 1/4 aa
#                  Bb x Bb -> 1/4 BB, 1/2 Bb, 1/4 bb
# Probability offspring is Aa Bb = (1/2) * (1/2) = 1/4
prob_AaBb = 0.25 * 0.25 * 4  # simplified: P(Aa) = 1/2, P(Bb) = 1/2 => 1/4

# Actually, P(Aa Bb) = 1/4 (Aa) * 1/4 (Bb) ??? Let's compute carefully:
# Aa x Aa offspring genotypes: AA(1/4), Aa(1/2), aa(1/4) => P(Aa)=1/2
# Bb x Bb: BB(1/4), Bb(1/2), bb(1/4) => P(Bb)=1/2
# So P(Aa Bb) = 1/2 * 1/2 = 1/4 

prob_AaBb = 0.25  # Wait double check: yes, 1/2*1/2=0.25

# Compute probability at least N Aa Bb using binomial distribution
prob = 0.0
for i in range(N, num_offspring + 1):
    prob += comb(num_offspring, i) * (prob_AaBb ** i) * ((1 - prob_AaBb) ** (num_offspring - i))

print("Your answer is:")
print(round(prob, 3))
