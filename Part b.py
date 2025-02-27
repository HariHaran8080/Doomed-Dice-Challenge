from collections import Counter
from itertools import product

def calculate_distribution():
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    
    sum_distribution = Counter(a + b for a, b in product(die_A, die_B))
    return sum_distribution

def calculate_probabilities(sum_distribution, total_combinations):
    probabilities = {k: v / total_combinations for k, v in sum_distribution.items()}
    return probabilities

def undoom_dice():
    sum_distribution = calculate_distribution()
    probabilities = calculate_probabilities(sum_distribution, 36)

    # New Die A with values <= 4
    new_die_A = [1, 2, 3, 4, 1, 2]

    # Compute New Die B to keep probability same
    new_die_B = [7 - face for face in new_die_A]

    print("\nNew Dice Values:")
    print(f"New Die A: {new_die_A}")
    print(f"New Die B: {new_die_B}")

    return new_die_A, new_die_B


new_die_A, new_die_B = undoom_dice()
