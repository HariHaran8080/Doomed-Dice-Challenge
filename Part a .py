from collections import Counter
from itertools import product

def calculate_combinations():
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    
    total_combinations = len(die_A) * len(die_B)  # 6 * 6 = 36
    print(f"Total possible combinations: {total_combinations}")
    
    return total_combinations

def calculate_distribution():
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    
    sum_distribution = Counter(a + b for a, b in product(die_A, die_B))
    print("\nSum distribution:")
    for key in sorted(sum_distribution.keys()):
        print(f"Sum {key}: {sum_distribution[key]} times")
    
    return sum_distribution

def calculate_probabilities(sum_distribution, total_combinations):
    probabilities = {k: v / total_combinations for k, v in sum_distribution.items()}
    print("\nProbability of each sum:")
    for key in sorted(probabilities.keys()):
        print(f"P(Sum={key}) = {probabilities[key]:.4f}")
    
    return probabilities


total_combinations = calculate_combinations()
sum_distribution = calculate_distribution()
probabilities = calculate_probabilities(sum_distribution, total_combinations)
