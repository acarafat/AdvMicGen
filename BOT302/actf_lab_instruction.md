# Lab Manual: Introduction to Sequence Assembly
## Objective
In this lab, you will learn the fundamentals of working in a command-line environment and perform a *de novo* genome assembly using Illumina (short) sequencing reads. You will then visualize the assembly graph and compare it to a pre-computed assembly generated from Nanopore (long) sequencing reads to understand the strengths and limitations of different sequencing technologies. Finally, you will calculate and compare quantitative assembly metrics like **N50**.
## Part 1: Software Setup and Server Connection
To perform sequence assembly, we will use a high-performance computing (HPC) cluster at Oregon State University. You cannot run these intensive tasks directly on your laptop, so you will remotely connect to the university's server.
### 1.1 Download and Install Required Software
- **File Transfer:** Download and install [FileZilla Client](https://filezilla-project.org/). We will use this to transfer files between your computer and the HPC server.
### 1.2 Connect to the Command Line
Depending on your operating system, follow the steps below to access the server's command line:
#### For Windows Users:
1. Download and install [PuTTY](https://www.putty.org/).
2. Open PuTTY. In the **Host Name** box, type: `shell.actf.oregonstate.edu`
3. Click **Open**. When prompted, enter your ONID username and password.
4. **Note:** You will likely be prompted for Duo Two-Factor Authentication (2FA) on your phone. Approve it to finish logging in.
5. Once signed in, select **ltpb_s26** ACTF class when prompted.
#### For Mac/Linux Users:
1. Open the **Terminal** application.
2. Connect by typing the following command (replace ONID with your actual username) and press Enter:
ssh ONID@shell.actf.oregonstate.edu
3. Enter your password when prompted (characters will not appear on the screen as you type—this is normal).
4. Approve the Duo Two-Factor Authentication (2FA) prompt sent to your phone.
5. Once signed in, select **ltpb_s26** ACTF class when prompted.
## Part 2: Introduction to UNIX Command Line Basics
Before we run our assembly, let's get familiar with a few basic UNIX commands. The command line is a text-based way to navigate files and run programs.
### Basic Commands:
- `pwd` (**P**rint **W**orking **D**irectory): Tells you exactly where you are.
- `ls` (**L**ist): Lists all files and folders in your current directory.
- `mkdir assembly_lab` (**M**ake **D**irectory): Creates a new folder.
- `cd assembly_lab` (**C**hange **D**irectory): Moves you inside a folder.
- `cd ..`: Moves you **up** one directory level.
### Task:

# 1. Inspect raw input files for assembly
```
cd /nfs5/ACTF/Course/ltpb_s26/data/week02_W
ls
```

# 2. Go back to your home folder
```
cd ~
```

# 3. Create a directory for today's lab and move into it
```
mkdir sequence_assembly
cd sequence_assembly
```

## Part 3: Short-Read Assembly with SPAdes
SPAdes is a popular genome assembler designed specifically for small genomes and short-read data (like Illumina).
> **Instructor Note:** The paths below (`/path/to/reads/...`) are placeholders. Replace it with actual raw input from data folder, i.e. `/nfs5/ACTF/Course/ltpb_s26/data/week02_W`
1. **Run the SPAdes Assembler:** We will provide SPAdes with our forward (_R1) and reverse (_R2) Illumina reads.
```
salloc -N 4 # Checking out four nodes
spades.py -1 /path/to/reads/illumina_R1.fastq.gz -2 /path/to/reads/illumina_R2.fastq.gz -o spades_output
```
2. **Wait for the assembly to finish:** Assembly is computationally intensive and may take several minutes.
3. **Check your output:**
```
cd spades_output
ls
```
Look for `assembly_graph.gfa` (for Bandage) and `contigs.fasta` (the assembled DNA sequences).
## Part 4: Visualizing and Transferring the Assembly Graph
Since we cannot view graphics in the terminal, we must transfer the .gfa file to your personal computer.
### 4.1 Connect via FileZilla
1. Open **FileZilla**.
2. Fill in the top connection details:
- **Host:** `sftp://shell.actf.oregonstate.edu` (the `sftp://` is required)
- **Username:** Your ONID username
- **Password:** Your ONID password
- **Port:** `22`
3. Click **Quickconnect**.
> **PRO-TIP for Two-Factor Authentication (2FA):**
If FileZilla times out, go to **File > Site Manager**. Create a **New Site**, but change the "Logon Type" to **Interactive**. Connect, and a window will pop up for your Duo prompt.
### 4.2 Transfer the Files
1. **Left Side (Local):** Navigate to your Desktop.
2. **Right Side (Server):** Navigate to `sequence_assembly/spades_output/`.
3. Drag and drop `assembly_graph.gfa` from the right to the left.
### 4.3 Visualize with Bandage
1. Open **Bandage**.
2. Go to **File > Load graph** and select `assembly_graph.gfa`.
3. Click **Draw graph** on the left panel.
4. Go to **File > Save image** to save your Illumina assembly plot.
## Part 5: Comparing Short-Read vs. Long-Read Assemblies
- **Short reads (Illumina):** Highly accurate but struggle with repetitive regions, resulting in a **fragmented** graph.
- **Long reads (Nanopore):** Higher error rates but can span repetitive regions, often resulting in a **single, circular** chromosome.
### 5.1 Transfer the Premade Flye Assembly
1. In FileZilla, navigate to the class shared folder: `/path/to/shared/data/` (provided by instructor).
2. Locate and download `flye_assembly.gfa`.
### 5.2 Visualize the Flye Assembly
1. Open **Bandage**, load `flye_assembly.gfa`, and click **Draw graph**.
2. Save a plot of this graph as well.
## Part 6: Evaluating Assembly Quality and Calculating N50
We use quantitative metrics to evaluate assemblies:
- **Total Length:** Sum of all assembled sequence lengths.
- **N50:** A measure of contiguity. The length of the shortest contig at 50% of the total assembly length. **Higher = More Continuous.**
### Run QUAST:
Return to your terminal and ensure you are in the `sequence_assembly` directory:
```
quast.py spades_output/contigs.fasta /path/to/shared/data/flye_assembly.fasta -o quast_results
```
# View the results
cat quast_results/report.txt
Locate the rows for **Total length** and **N50** in the table.
## Lab Assignment & Discussion Questions
Include the images of both your SPAdes and Flye plots in your report and answer the following:
1. **Visual Comparison:** Describe the differences between the SPAdes (Illumina) and Flye (Nanopore) graphs. How many separate nodes (pieces) are visible in each?
2. **Assembly Statistics:** Based on the QUAST report, what are the Total Length and N50 values for both assemblies?
3. **Interpreting N50:** Which technology resulted in a more contiguous assembly? Does this match your visual observation in Bandage?
4. **Repeats:** Why do short Illumina reads struggle with repetitive DNA sequences?


