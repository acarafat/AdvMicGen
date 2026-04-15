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
1. Download and install [PuTTY](https://putty.org/index.html).

![https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture1.png?raw=true](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture1.png?raw=true)

3. Open PuTTY. In the **Host Name** box, type: `shell.actf.oregonstate.edu`
4. Click **Open**. When prompted, enter your ONID username and password.
5. **Note:** You will likely be prompted for Duo Two-Factor Authentication (2FA) on your phone. Approve it to finish logging in.
6. Once signed in, select **ltpb_s26** ACTF class when prompted.

![https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture2.png?raw=true](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture2.png?raw=true)

#### For Mac/Linux Users:
1. Open the **Terminal** application.
2. Connect by typing the following command (replace ONID with your actual username) and press Enter:
```
ssh ONID@shell.actf.oregonstate.edu
```
3. Enter your password when prompted (characters will not appear on the screen as you type—this is normal).
4. Approve the Duo Two-Factor Authentication (2FA) prompt sent to your phone.
5. Once signed in, select **ltpb_s26** ACTF class when prompted.

![https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture3.png?raw=true](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture3.png?raw=true)

## Part 2: Introduction to UNIX Command Line Basics
Before we run our assembly, let's get familiar with a few basic UNIX commands. The command line is a text-based way to navigate files and run programs.
### Basic Commands:
- `pwd` (**P**rint **W**orking **D**irectory): Tells you exactly where you are.
- `ls` (**L**ist): Lists all files and folders in your current directory.
- `mkdir assembly_lab` (**M**ake **D**irectory): Creates a new folder.
- `cd assembly_lab` (**C**hange **D**irectory): Moves you inside a folder.
- `cd ..`: Moves you **up** one directory level.

### Tasks:

#### 1. Inspect raw input files for assembly
```
cd /nfs5/ACTF/Course/ltpb_s26/data/week02_W
ls
```

#### 2. Go back to your home folder
```
cd ~
```

#### 3. Create a directory for today's lab and move into it
```
mkdir sequence_assembly
cd sequence_assembly
```

#### 4. Let's play an UNIX game
Little Brother is missing! He must have run off in last night's storm.

In this Exercise we will practice navigating a file system using a command line interface. That could be pretty boring - and therefore hard to practice. Dr. Jesse Zaneveld has put together a set of files and folders that you can download that tell a story. In this case, it's a story of your little brother, who has left your village on his bike and headed for the spooooooooky mansion up the hill.

Each directory will represent a certain place (the village, your house, a secret passageway, etc) and the text files in them will represent things you can find (a unicorn, a magical mushroom, your lost brother).

Your goal is to map the mansion, find your brother, and move the little_brother.txt file back to the folder representing your home in the village. Along the way you can also find the sword Excalibur, return a lost animal to the zoo, and assemble ingredients for a tasty mushroom stew.

In accomplishing this goal, you are only allowed to use commands that you type into your command line interface. After all, that's the point :).

![https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture4.jpg?raw=true](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/Picture4.jpg?raw=true)

Game set-up: Copy the game file in your working directory, extract it.

```
cd
cp /nfs5/ACTF/Course/ltpb_s26/data/activity_directory_treasure_hunt.zip .
unzip activity_directory_treasure_hunt.zip
ls
```

You will see an new directory, `activity_2_directory_treasure_hunt`. Go to the directory and follow instructions.

Check out the folders. You may want to read the stuff in the home_sweet_home folder and the_zoo first.

```
cd activity_2_directory_treasure_hunt
less instructions.txt
```

When you find your little brother (represented by 'little_brother.txt') you can move it back to your starting location using mv commands. For example, mv little_brother.txt .. moves his text file into the enclosing directory.

## Part 3: Short-Read Assembly with SPAdes
SPAdes is a popular genome assembler designed specifically for small genomes and short-read data (like Illumina).
> **Instructor Note:** The paths below (`/path/to/reads/...`) are placeholders. Replace it with actual raw input from data folder, i.e. `/nfs5/ACTF/Course/ltpb_s26/data/week02_W`
1. **Run the SPAdes Assembler:** We will provide SPAdes with our forward (_R1) and reverse (_R2) Illumina reads.
```
salloc -N 4 # Checking out four nodes
spades.py -1 ~/../../data/week02_W/19AcAY341.1.2_R1_fastp_filtered.fastq.gz -2 ~/../../data/week02_W/19AcAY341.1.2_R2_fastp_filtered.fastq.gz -o spades_output
```
2. **Wait for the assembly to finish:** Assembly is computationally intensive and may take several minutes.
3. **Check your output:**
```
cd spades_output
ls
```
Look for `assembly_graph.gfa` (for Bandage) and `contigs.fasta` (the assembled DNA sequences).
## Part 4: Visualizing the Assembly Graph via Command Line
We will use the command-line version of Bandage to generate an image of our assembly graph directly on the server.
### 4.1 Generate the Plot
While inside your `spades_output` directory, run the following command to create a PNG image of your assembly:
```
Bandage plot assembly_graph_with_scaffolds.gfa spades_plot.png
```
### 4.2 Generate the Long-Read Plot
Your instructor has pre-computed a long-read assembly. Generate a plot for that assembly as well (replace the path with the one provided in class):

```
Bandage plot ~/../../data/week02_W/long_only_assem/assembly_graph.gfa flye_plot.png
```

## Part 5: Transferring Results to Your Computer

### 5.1 Connecting with FileZilla
Open FileZilla.
Fill in the connection details:
```
Host: sftp://shell.actf.oregonstate.edu
Username: Your ONID username
Password: Your ONID password
Port: 22
```

Click Quickconnect.

Two-Factor Authentication (2FA): If FileZilla times out, go to File > Site Manager. Create a New Site, set "Logon Type" to Interactive, and connect.

### 5.2 Transfer the Files

Left Side (Local): Navigate to your `Desktop` or other destination.
Right Side (Server): Navigate to `sequence_assembly/spades_output/`.
Drag and drop spades_plot.png and flye_plot.png to your computer.

## Part 6: Evaluating Assembly Quality and Calculating N50
We use quantitative metrics to evaluate assemblies:
- **Total Length:** Sum of all assembled sequence lengths.
- **N50:** A measure of contiguity. The length of the shortest contig at 50% of the total assembly length. **Higher = More Continuous.**
### Run QUAST:
Return to your terminal and ensure you are in the `sequence_assembly` directory:
```
quast.py spades_output/contigs.fasta -o quast_shortread_results
quast.py ~/../../data/week02_W/long_only_assem/flye_assembly.fasta -o quast_longread_results
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

**Illumina Assembly Bandage Plot:**
![Illumina Bandage](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/graph.png?raw=true)

**Nanopore Assembly Bandage Plot:**
![Nanopore Bandage](https://github.com/acarafat/AdvMicGen/blob/main/BOT302/nanopore_assembly.png?raw=true)
