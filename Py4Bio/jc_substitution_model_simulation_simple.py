import random
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate a random DNA sequence of 1000 bp
bases = ['A', 'T', 'G', 'C']
original_sequence = []
for _ in range(1000):
    original_sequence.append(random.choice(bases))

mutated_sequence = original_sequence.copy()

# Step 2: Simulate 2000 rounds of mutations
mutation_counts = []
for i in range(1, 2001):
    pos = random.randint(0, 999)
    current_base = mutated_sequence[pos]
    new_base = random.choice(bases)  # Any mutation has 25% chance including no-change
    mutated_sequence[pos] = new_base

    # Step 3: Count differences from original
    differences = 0
    for a, b in zip(original_sequence, mutated_sequence):
        if a != b:
            differences += 1
    mutation_counts.append(differences)

# Step 4: Plot raw mutation counts and save
plt.figure(figsize=(10, 5))
plt.plot(range(1, 2001), mutation_counts, label='Observed differences')
plt.xlabel('Mutation rounds')
plt.ylabel('Number of differences')
plt.title('Accumulated observed mutations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("observed_mutations.png")

# Step 5: Apply Jukes-Cantor correction
corrected_mutations = []
for obs_diff in mutation_counts:
    d = obs_diff / 1000
    if d < 0.75:
        D = -0.75 * np.log(1 - (4 / 3) * d)
        corrected_mutations.append(D * 1000)
    else:
        corrected_mutations.append(np.nan)  # Beyond JC model's range

# Step 6: Plot corrected mutations and save
plt.figure(figsize=(10, 5))
plt.plot(range(1, 2001), corrected_mutations, color='orange', label='Jukes-Cantor corrected')
plt.xlabel('Mutation rounds')
plt.ylabel('Corrected number of substitutions')
plt.title('Corrected mutation estimate using Jukes-Cantor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("jukes_cantor_corrected.png")

print("Figures are saved! Please check observed_mutations.png and jukes_cantor_corrected.png")
