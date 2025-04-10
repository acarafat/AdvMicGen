import random
import matplotlib.pyplot as plt
import numpy as np

def generate_random_dna(length=1000):
    bases = ['A', 'T', 'G', 'C']
    return [random.choice(bases) for _ in range(length)]

def mutate_sequence(seq):
    bases = ['A', 'T', 'G', 'C']
    pos = random.randint(0, len(seq) - 1)
    current_base = seq[pos]
    new_base = random.choice([b for b in bases if b != current_base])
    mutated_seq = seq.copy()
    mutated_seq[pos] = new_base
    return mutated_seq

def count_differences(seq1, seq2):
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

def simulate_mutations(original_seq, rounds=10000):
    mutated_seq = original_seq.copy()
    mutation_counts = []

    for _ in range(rounds):
        mutated_seq = mutate_sequence(mutated_seq)
        diff = count_differences(original_seq, mutated_seq)
        mutation_counts.append(diff)

    return mutation_counts

def jukes_cantor_correction(mutation_counts, length):
    corrected = []
    for count in mutation_counts:
        d = count / length
        if d < 0.75:
            D = -0.75 * np.log(1 - (4/3) * d)
            corrected.append(D * length)
        else:
            corrected.append(np.nan)
    return corrected

def save_plot(x, y, title, ylabel, label, filename, color='blue'):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color=color, label=label)
    plt.xlabel('Mutation rounds')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def main():
    try:
        length = int(input("Enter the length of the DNA sequence: "))
        rounds = int(input("Enter the number of mutation generations: "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    original = generate_random_dna(length)
    mutation_data = simulate_mutations(original, rounds)

    save_plot(
        x=range(1, rounds + 1),
        y=mutation_data,
        title='Accumulated Observed Mutations',
        ylabel='Number of differences',
        label='Observed differences',
        filename='observed_mutations.png',
        color='blue'
    )

    corrected_data = jukes_cantor_correction(mutation_data, length)

    save_plot(
        x=range(1, rounds + 1),
        y=corrected_data,
        title='Corrected Mutations Using Jukes-Cantor Model',
        ylabel='Corrected number of substitutions',
        label='Jukes-Cantor corrected',
        filename='jukes_cantor_correction.png',
        color='orange'
    )

    print("Simulation completed.")
    print("Plots saved as 'observed_mutations.png' and 'jukes_cantor_correction.png'.")

if __name__ == "__main__":
    main()
