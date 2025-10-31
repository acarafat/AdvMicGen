import matplotlib.pyplot as plt

# load sequence
seq0 = "GCCCGTGTGGGCCACGCCCTGCCTCCCCAGTCCCCACCCTCACCGGCCCGCCTCGCTCGCCCGCGCGCGCGCGCGCGACGTGCATGGCGCGCGGCCTCCTCCCCCCCTCCCGCCGCTATATATACCCCTCCCTTGCAACCGCCTCCTCTCATCGCACACTCCAAGCTAAGCCTAAGCGAGCGAGAAAAAATAGCAAAAGCTAGCCGGCAAGCAACGCCAACTAATTAGGGGAGAGAGATATTCATGGCTCCGGCGGCGGTGGCTGCGGCGGAGGCGGGGTCGAAGGCGGCGGCGGTGGCG"


# define base stacking energy
stacking_energy = {'AA':-5, 'AC':-10, 'AG':-6, 'AT':-6,
                   'CA':-6, 'CC':-8, 'CG':-9, 'CT':-6,
                   'GA':-9, 'GC':-14, 'GG':-8, 'GT':-10,
                   'TA':-3, 'TC':-9, 'TG':-6, 'TT':-5}

# takes input of a sequence
# returns an array of base stacking energy in all dinucleotide positions
def make_stacking_energy_array(seq):
    base_stacking_energy_array = []

    for i in range(0, len(seq)-1):
        dinucleotide = seq[i:i+2]
        energy = stacking_energy[dinucleotide]
        base_stacking_energy_array.append(energy)

    return base_stacking_energy_array


def make_window_base_stacking_array(base_stacking_energy_array, window_size):
    window_base_stacking_array = []

    for i in range(0, len(base_stacking_energy_array) - (window_size - 1)):
        window_subset = base_stacking_energy_array[i:i+window_size]
        total_window_energy = sum(window_subset)

        window_base_stacking_array.append(total_window_energy)

    return window_base_stacking_array



if __name__ == "__main__":
    test_array = make_stacking_energy_array(seq0)
    base_stacking_window = make_window_base_stacking_array(test_array, 20)

    plt.plot(range(1, len(base_stacking_window)+1 ), base_stacking_window)
    plt.show()