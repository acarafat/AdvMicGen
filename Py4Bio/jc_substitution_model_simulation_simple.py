import random
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate a random DNA sequence of 1000 bp
bases = ['A', 'T', 'G', 'C']
original_sequence = [random.choice(bases) for _ in range(1000)]
mutated_sequence = original_sequence.copy()

# Step 2: Simulate 10,000 rounds of mutations
mutation_counts = []
for i in range(1, 2001):
    pos = random.randint(0, 999)
    current_base = mutated_sequence[pos]
    new_base = random.choice(bases) # Any mutation has 25% chance including no-change
    mutated_sequence[pos] = new_base
    # Step 3: Count differences from original
    differences = sum(1 for a, b in zip(original_sequence, mutated_sequence) if a != b)
    mutation_counts.append(differences)

# Step 4: Plot raw mutation counts
plt.figure(figsize=(10, 5))
plt.plot(range(1, 2001), mutation_counts, label='Observed differences')
plt.xlabel('Mutation rounds')
plt.ylabel('Number of differences')
plt.title('Accumulated observed mutations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Apply Jukes-Cantor correction
# JC: D = -3/4 * ln(1 - 4d/3)
# where d = observed differences / length
corrected_mutations = []
for obs_diff in mutation_counts:
    d = obs_diff / 1000
    if d < 0.75:
        D = -0.75 * np.log(1 - (4/3)*d)
    else:
        D = np.nan  # beyond JC model's range
    corrected_mutations.append(D * 1000 if not np.isnan(D) else np.nan)

# Step 6: Plot corrected mutations
plt.figure(figsize=(10, 5))
plt.plot(range(1, 10001), corrected_mutations, color='orange', label='Jukes-Cantor corrected')
plt.xlabel('Mutation rounds')
plt.ylabel('Corrected number of substitutions')
plt.title('Corrected mutation estimate using Jukes-Cantor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
