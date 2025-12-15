# ============================================================
# ROSALIND PROBLEM: IPRB - Expected Dominant Offspring
# INPUT: Six integers representing number of couples for each genotype pairing
# OUTPUT: Expected number of offspring displaying the dominant phenotype
# ============================================================

# Paste your input here
couples = [17014, 19579, 16980, 17261, 18225, 17338]  # AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

# ------------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE
# ------------------------------------------------------------

# Each couple has exactly 2 offspring
offspring_per_couple = 2

# Probability that an offspring has dominant phenotype for each genotype pair
# Order: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
dominant_probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

# Compute expected dominant offspring
expected_dominant = sum(c * offspring_per_couple * p for c, p in zip(couples, dominant_probs))

print("Your answer is:")
print(expected_dominant)
