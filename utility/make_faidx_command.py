#!/bin/python3

from sys import argv


# Usage:
#   python script_name.py positions.txt genome.fasta
#
# Description:
#   Given a tab-delimited position file (`positions.txt`) with sequence IDs and start-end coordinates,
#   this script selects the longest region per genome (based on sequence ID prefix before the last underscore),
#   formats coordinates properly, and writes a shell script `faidx_command.sh` containing `samtools faidx` commands
#   to extract those regions from the provided FASTA file (`genome.fasta`).

def main(position_file, target_fasta):
   '''
   INPUT: position file for samtools faidx
   OUTPUT: command file for running samtools faidx
   '''
   unique = {}
   command = ''

   with open(position_file) as handle:
      raw = handle.readlines()

   for i in raw:
      seq_id, m, n = i.split() # m is start position, n is end position
      genome_id = seq_id.rsplit('_', 1)[0]
      if genome_id not in unique.keys():
            unique[genome_id] = [seq_id, m, n, abs(int(m)-int(n)), '+']
      else:
         if abs(int(m)-int(n)) > unique[genome_id][3]: # If multiple hits for the same seq_id, keep the longest
            unique[genome_id] = [seq_id, m, n, abs(int(m)-int(n)), '+']

      if int(unique[genome_id][1]) > int(unique[genome_id][2]):
         unique[genome_id] = [seq_id, n, m, abs(int(m)-int(n)), '-']

   for k in unique.keys():
      if k[3]== "+":
            command += f"samtools faidx {target_fasta} {unique[k][0]}:{unique[k][1]}-{unique[k][2]}\n"
      else:
            command += f"samtools faidx {target_fasta} {unique[k][0]}:{unique[k][1]}-{unique[k][2]} -i\n"

   with open('faidx_command.sh','w') as handle:
      handle.write(command)

   pass



if __name__ == "__main__":
   if len(argv) != 3:
       print("Error: Missing required arguments.\n")
       print("Usage:")
       print("  python script_name.py positions.txt genome.fasta\n")
       print("Description:")
       print("  Given a tab-delimited position file (`positions.txt`) with sequence IDs and start-end coordi
nates,")
       print("  this script selects the longest region per genome (based on sequence ID prefix before the la
st underscore),")
       print("  formats coordinates properly, and writes a shell script `faidx_command.sh` containing `samto
ols faidx`")
       print("  commands to extract those regions from the provided FASTA file (`genome.fasta`).")
       exit(1)
   main(argv[1], argv[2])
