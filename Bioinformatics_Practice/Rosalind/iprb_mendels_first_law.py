#!/usr/bin/env python3
"""
Rosalind Problem: IPRB (Mendel's First Law)
Problem ID: IPRB
URL: http://rosalind.info/problems/iprb/

Given: Positive integers k (AA), m (Aa), n (aa)
Return: Probability that two randomly selected mating organisms 
        produce offspring with dominant phenotype.
"""

def dominant_probability(k: int, m: int, n: int) -> float:
    """
    Calculates probability of dominant phenotype offspring.
    
    Args:
        k: Number of homozygous dominant (AA) organisms
        m: Number of heterozygous (Aa) organisms  
        n: Number of homozygous recessive (aa) organisms
    
    Returns:
        float: Probability of offspring with dominant phenotype
    """
    total = k + m + n
    
    # Total possible pair combinations
    total_pairs = total * (total - 1)
    
    # Calculate probabilities of getting recessive offspring
    # 1. aa × aa: always recessive
    recessive_from_nn = n * (n - 1)
    
    # 2. aa × Aa: 50% chance recessive
    recessive_from_na = n * m  # (n×m + m×n) but ×0.5 later
    
    # 3. Aa × Aa: 25% chance recessive  
    recessive_from_mm = m * (m - 1) * 0.25
    
    # 4. aa × AA: 0% recessive (dominant always)
    # 5. AA × Aa: 0% recessive
    # 6. AA × AA: 0% recessive
    
    # Total recessive probability
    total_recessive = (recessive_from_nn + recessive_from_na + recessive_from_mm)
    recessive_prob = total_recessive / total_pairs
    
    # Dominant probability = 1 - recessive probability
    return 1 - recessive_prob

def main():
    # Read input (paste your dataset here)
    # Format: three integers k m n
    data = "19 16 24"  # REPLACE WITH YOUR DATASET
    
    # Parse k, m, n
    k_str, m_str, n_str = data.split()
    k = int(k_str)
    m = int(m_str)
    n = int(n_str)
    
    # Calculate probability
    prob = dominant_probability(k, m, n)
    
    # Print with 5 decimal places (as in sample)
    print(f"{prob:.5f}")
    
    # Optional: Save output
    # with open('iprb_output.txt', 'w') as f:
    #     f.write(f"{prob:.5f}")

if __name__ == "__main__":
    main()