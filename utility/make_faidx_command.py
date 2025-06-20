#!/bin/python3

from sys import argv


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
      seq_id, m, n = i.split()
      genome_id = seq_id.rsplit('_', 1)[0]
      if genome_id not in unique.keys():
            unique[genome_id] = [seq_id, m, n, abs(int(m)-int(n))]
      else:
         if abs(int(m)-int(n)) > unique[genome_id][3]:
            unique[genome_id] = [seq_id, m, n, abs(int(m)-int(n))]
      if int(unique[genome_id][1]) > int(unique[genome_id][2]):
         unique[genome_id] = [seq_id, n, m, abs(int(m)-int(n))]

   for k in unique.keys():
      command += f"samtools faidx {target_fasta} {unique[k][0]}:{unique[k][1]}-{unique[k][2]}\n"

   with open('faidx_command.sh','w') as handle:
      handle.write(command)

   pass


if __name__ == "__main__":
   main(argv[1], argv[2])
