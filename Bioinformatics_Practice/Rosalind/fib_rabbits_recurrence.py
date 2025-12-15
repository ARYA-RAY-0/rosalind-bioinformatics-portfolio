#!/usr/bin/env python3
"""
Rosalind Problem: FIB (Rabbits and Recurrence Relations)
Problem ID: FIB
URL: http://rosalind.info/problems/fib/

Given: Positive integers n ≤ 40 and k ≤ 5.
Return: Total rabbit pairs after n months starting with 1 pair,
        where each mature pair produces k offspring pairs per month.
"""

def rabbit_pairs(n: int, k: int) -> int:
    """
    Calculates rabbit population growth using recurrence:
    F(n) = F(n-1) + k * F(n-2)

    Args:
        n (int): Number of months.
        k (int): Offspring pairs produced per mature pair per month.

    Returns:
        int: Total rabbit pairs after n months.
    """
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 1

    # Initialize for months 1 and 2
    prev1, prev2 = 1, 1  # F(n-1), F(n-2)

    # Calculate from month 3 to n
    for month in range(3, n + 1):
        current = prev1 + k * prev2
        # Shift values for next iteration
        prev2, prev1 = prev1, current

    return prev1

def main():
    # Read input (paste your dataset here)
    # Example: "5 3"
    data = "35 4"  # REPLACE WITH YOUR DATASET

    # Parse n and k
    n_str, k_str = data.split()
    n = int(n_str)
    k = int(k_str)

    # Calculate result
    result = rabbit_pairs(n, k)

    # Print result
    print(result)

    # Optional: Save output
    # with open('fib_output.txt', 'w') as f:
    #     f.write(str(result))

if __name__ == "__main__":
    main()