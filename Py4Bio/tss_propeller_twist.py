import matplotlib.pyplot as plt
import tss_base_stacking

# load sequence
seq0 = "GCCCGTGTGGGCCACGCCCTGCCTCCCCAGTCCCCACCCTCACCGGCCCGCCTCGCTCGCCCGCGCGCGCGCGCGCGACGTGCATGGCGCGCGGCCTCCTCCCCCCCTCCCGCCGCTATATATACCCCTCCCTTGCAACCGCCTCCTCTCATCGCACACTCCAAGCTAAGCCTAAGCGAGCGAGAAAAAATAGCAAAAGCTAGCCGGCAAGCAACGCCAACTAATTAGGGGAGAGAGATATTCATGGCTCCGGCGGCGGTGGCTGCGGCGGAGGCGGGGTCGAAGGCGGCGGCGGTGGCG"


# define base propeller twist
stacking_energy = {'AA':-18, 'AC':-13, 'AG':-14, 'AT':-15,
                   'CA':-9, 'CC':-8, 'CG':-10, 'CT':-14,
                   'GA':-13, 'GC':-11, 'GG':-8, 'GT':-13,
                   'TA':-11, 'TC':-13, 'TG':-9, 'TT':-18}




if __name__ == "__main__":
    window_size = 20
    propeller_twist_array = tss_base_stacking.make_stacking_energy_array(seq0)
    propeller_twist_window_array = tss_base_stacking.make_window_base_stacking_array(propeller_twist_array, window_size)

    propeller_twist_data = ''
    for data in propeller_twist_window_array:
        propeller_twist_data += str(data)+"\n"

    fh = open('propeller_twist_data.txt', 'w'ß)
    fh.write(propeller_twist_data)
    fh.close()

    plt.plot(range(1, len(propeller_twist_window_array)+1 ), propeller_twist_window_array)
    plt.show()
    

    