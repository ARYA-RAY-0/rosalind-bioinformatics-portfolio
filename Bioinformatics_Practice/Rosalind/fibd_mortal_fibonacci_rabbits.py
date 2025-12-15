# ============================================================
# ROSALIND PROBLEM: FIBD - Mortal Fibonacci Rabbits
# INPUT: Two integers n (months) and m (lifespan in months)
# OUTPUT: Total number of rabbit pairs after n months
# ============================================================

# Paste your input values here
n = 81   # number of months
m = 19   # lifespan of rabbits in months

# ------------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE
# ------------------------------------------------------------

# ages[i] = number of rabbit pairs of age i months
ages = [0] * m
ages[0] = 1  # Month 1: one newborn pair

for month in range(1, n):
    newborns = sum(ages[1:])  # only rabbits age >=1 reproduce
    ages = [newborns] + ages[:-1]  # age everyone, oldest die off

# Total rabbits alive after n months
print("Your Rosalind answer is:")
print(sum(ages))
