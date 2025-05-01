## Worksheet: Introduction to Unix/Bash for Bioinformatics

**Objective:** To familiarize yourself with the Unix/Bash command-line interface (CLI) and learn basic commands essential for bioinformatics analysis.

**Why Unix/Bash in Bioinformatics?**
Bioinformatics often involves working with very large datasets (genome sequences, gene expression data, protein structures, etc.). Graphical user interfaces (GUIs) can become slow, inefficient, or lack the specific tools needed for these complex tasks. The command line provides a powerful, efficient, scriptable, and reproducible way to:

* Navigate complex file systems containing sequencing data, reference genomes, etc.
* Manage and manipulate large text files (like FASTA, FASTQ, VCF, GFF).
* Automate repetitive analysis steps using scripts.
* Run specialized bioinformatics software (most are designed primarily for command-line use).
* Connect different tools together in analysis pipelines.

---

### Part 1: The Command Line Interface (CLI) & Basic Navigation

The command line is a text-based way to interact with your computer. You type commands, press Enter, and the system responds. You'll see a *prompt*, often ending in `$` or `#`, indicating it's ready for your input.

**Key Commands:**

1.  `pwd` (Print Working Directory)
    * Shows the full path of the directory you are currently located in.
    ```bash
    pwd
    ```
    *Example Output:* `/home/student/bio_project`

2.  `ls` (List)
    * Lists the files and directories in the current directory.
    * `ls`: Basic, simple listing.
    * `ls -l`: **L**ong listing format (shows permissions, owner, size, modification date).
    * `ls -lh`: Long listing with **h**uman-readable file sizes (e.g., KB, MB, GB). Very useful!
    * `ls -lt`: Files ordered based on the time they were last changed.
    * `ls -a`: Lists **a**ll files, including hidden files (names starting with a dot `.`, like configuration files).
    ```bash
    ls
    ls -lh
    ls -a
    ```

3.  `cd` (Change Directory)
    * Used to move between directories (folders).
    * `cd <directory_name>`: Moves into a subdirectory named `<directory_name>`. (e.g., `cd raw_data`)
    * `cd ..`: Moves one level **up** (to the parent directory).
    * `cd ~` or just `cd`: Moves to your **home** directory (your personal starting point).
    * `cd /`: Moves to the **root** directory (the top-level directory of the entire system).
    * *Tip:* Use the `Tab` key to auto-complete directory and file names!

    ```bash
    # Assume you are in /home/student and have a directory 'bio_project'
    pwd
    cd bio_project
    pwd # Check your new location
    cd .. # Go back up to /home/student
    pwd # Check again
    cd ~ # Go to your home directory
    pwd
    ```

**Exercise 1:**
a. Use `pwd` to find out where you are right now.
b. Use `ls -lh` to see what's in your current directory. Note the file sizes.
c. If there's a directory listed, use `cd` to move into it. Use `pwd` again.
d. Use `cd ..` to move back up.
e. Use `cd ~` to ensure you are in your home directory.

---

### Part 2: Working with Files and Directories

**Key Commands:**

1.  `mkdir <directory_name>` (Make Directory)
    * Creates a new, empty directory.
    ```bash
    # Create directories for a typical project structure
    mkdir project_alpha
    cd project_alpha
    mkdir raw_data results scripts reference_genomes
    ls # You should see the new directories
    ```

2.  `touch <filename>`
    * Creates an empty file if it doesn't exist.
    * If the file *does* exist, it updates the file's last modification time (useful for some tools).
    ```bash
    cd scripts
    touch analysis_pipeline.sh
    touch notes.txt
    ls -l # See the new empty files with size 0
    ```

3.  `cp <source_file> <destination>` (Copy)
    * Copies a file.
    * `cp file1 file2`: Copies `file1` to `file2` in the current directory.
    * `cp file1 directory/`: Copies `file1` into the `directory`.
    * `cp file1 directory/new_name`: Copies `file1` into `directory` and gives it a `new_name`.
    * `cp -r <source_directory> <destination_directory>`: Copies a directory **r**ecursively (including all its contents).
    ```bash
    # Assuming you're in project_alpha/scripts
    cp notes.txt notes_backup.txt
    ls
    cd .. # Go up to project_alpha
    cp scripts/notes.txt results/ # Copy notes into the results directory
    ls results/
    ```

4.  `mv <source> <destination>` (Move / Rename)
    * Moves a file or directory to a new location OR renames it if the destination is in the same directory.
    ```bash
    # Rename notes_backup.txt to old_notes.txt (in scripts directory)
    cd scripts
    mv notes_backup.txt old_notes.txt
    ls

    # Move old_notes.txt to the results directory (go up first)
    cd ..
    mv scripts/old_notes.txt results/
    ls scripts/ # old_notes.txt should be gone
    ls results/ # old_notes.txt should be here
    ```

5.  `rm <filename>` (Remove)
    * Deletes a file. **USE WITH EXTREME CAUTION! There is usually NO UNDO or trash bin.** Double-check before pressing Enter.
    * `rm -f <file_name>`: Removes a file without confirming to the user. **CAUTION**
    * `rm -r <directory_name>`: Removes a directory and all its contents **r**ecursively. **EVEN MORE CAUTION!**
    * `rm -i <filename>`: Interactive mode, prompts for confirmation before deleting each file. Safer option.
    ```bash
    # Be careful! Let's remove the backup file in results
    rm results/old_notes.txt
    # Or safer:
    # rm -i results/old_notes.txt # Asks 'remove regular empty file results/old_notes.txt?'
    ```

6.  `cat <filename>` (Concatenate)
    * Displays the entire content of one or more files to the screen. Good for small files.
    ```bash
    # First, put some text in notes.txt (we'll use a simple way for now)
    echo "Project Alpha Notes" > results/notes.txt # '>' overwrites the file
    echo "Analysis started: $(date)" >> results/notes.txt # '>>' appends to the file
    cat results/notes.txt
    ```

7.  `less <filename>`
    * Views file content page by page. Essential for large bioinformatics files (like FASTQ or VCF) that won't fit on the screen.
    * **Navigation:** Use arrow keys (Up/Down), PageUp/PageDown, Spacebar (next page), `b` (back one page).
    * **Search:** Type `/` followed by your search term, press Enter. `n` finds the next match, `N` finds the previous.
    * **Quit:** Press `q`.
    ```bash
    # Imagine notes.txt was very long
    less results/notes.txt
    # (Press 'q' to exit less)
    ```

8.  `head <filename>`
    * Displays the first few lines of a file (default is 10).
    * `head -n 5 <filename>`: Shows the first 5 lines. Useful for checking file headers (e.g., in FASTA or VCF files).
    ```bash
    # Let's create a sample FASTA file in raw_data
    echo ">Seq1_OrganismA_GeneX" > raw_data/sample.fasta
    echo "ATGCGTAGCTAGCTAGCATGCGTAGCTAGCTAGCATG" >> raw_data/sample.fasta
    echo "CGTAGCTAGCTAGCTAGCTACGTACGTACGTACGTAC" >> raw_data/sample.fasta
    echo ">Seq2_OrganismB_GeneY" >> raw_data/sample.fasta
    echo "TTTTACGTAGCATGCATGCATTTTACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "AAAAACGTAGCATGCATGCAAAAAACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "GGGGACGTAGCATGCATGCAGGGGACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "CCCCACGTAGCATGCATGCACCCCACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "NNNNACGTAGCATGCATGCANNNNACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "ATATACGTAGCATGCATGCAATATACGTAGCATGCAT" >> raw_data/sample.fasta
    echo "GCGCACGTAGCATGCATGCAGCGCACGTAGCATGCAT" >> raw_data/sample.fasta
    echo ">Seq3_OrganismA_GeneZ" >> raw_data/sample.fasta
    echo "GATTACAGATTACAGATTACAGATTACAGATTACAGA" >> raw_data/sample.fasta

    head raw_data/sample.fasta
    head -n 4 raw_data/sample.fasta # Show first 4 lines (2 headers, 2 sequence lines)
    ```

9.  `tail <filename>`
    * Displays the last few lines of a file (default is 10).
    * `tail -n 3 <filename>`: Shows the last 3 lines. Useful for checking if a long process finished correctly or seeing the end of large files.
    ```bash
    tail raw_data/sample.fasta
    tail -n 3 raw_data/sample.fasta # Show the last header and sequence lines
    ```

**Exercise 2:**
a. Navigate into the `project_alpha/reference_genomes` directory.
b. Create an empty file named `human_genome.fasta` (it's empty for now, we'll download later).
c. Copy the `sample.fasta` file from `raw_data` into the current directory (`reference_genomes`).
d. Rename the copied `sample.fasta` in this directory to `test_sequences.fasta`.
e. View the first 2 lines of `test_sequences.fasta`.
f. View the last 2 lines of `test_sequences.fasta`.
g. Delete the empty `human_genome.fasta` file using `rm`.

---

### Part 3: Downloading Files (`wget`)

`wget` is a command-line utility to download files from web or FTP servers. Essential for getting reference genomes, annotations, software, etc.

**Syntax:** `wget <URL>`

```bash
# Let's download a small sample protein FASTA file from UniProt
# We'll put it in the reference_genomes directory
cd ~/project_alpha/reference_genomes # Make sure you're in the right place

# Download the Insulin sequence for Human (P01308)
# Note: URLs can change over time. This is for demonstration.
wget [https://rest.uniprot.org/uniprotkb/P01308.fasta](https://rest.uniprot.org/uniprotkb/P01308.fasta)

# Check if the file was downloaded
ls -lh P01308.fasta

# View the downloaded file
less P01308.fasta # (Press 'q' to quit)

# Rename it for clarity
mv P01308.fasta human_insulin.fasta
ls -lh
```

**Exercise 3:**
a. Navigate to the `project_alpha/raw_data` directory.
b. Use `wget` to download the FASTA sequence for Yeast Mbp1 transcription factor (UniProt ID P39678): `https://rest.uniprot.org/uniprotkb/P39678.fasta`
c. Rename the downloaded file `P39678.fasta` to `yeast_mbp1.fasta`.
d. Use `head` to look at the first 5 lines of the downloaded file.

---

### Part 4: The Unix Philosophy & Piping (`|`)

**The Philosophy (Simplified):**
1.  Write programs that do **one thing** and do it well. (`ls` lists, `grep` searches, `wc` counts).
2.  Write programs to **work together**.
3.  Write programs to handle **text streams**, because that is a universal interface.

**Piping (`|`):** The pipe symbol `|` is one of the most powerful concepts. It connects the *standard output* (stdout - the normal text output) of one command directly to the *standard input* (stdin) of the next command. This lets you chain simple tools to perform complex tasks without creating temporary intermediate files.

**Example:** Count the number of sequences in a FASTA file.
FASTA sequence headers usually start with `>`. We can find these lines (`grep`) and then count how many lines were found (`wc -l`).

```bash
# Using the sample.fasta file from Part 2 (in raw_data)
cd ~/project_alpha/raw_data

# 1. Find lines starting with '>' using grep
grep "^>" sample.fasta # '^' means 'start of line'

# 2. Count the number of lines found using wc (word count)
#    wc -l counts lines
grep "^>" sample.fasta | wc -l
```
Here, the output of `grep "^>" sample.fasta` (which is the list of header lines) is *piped* directly as input to `wc -l`, which counts them. The result `3` appears on the screen.

**Exercise 4:**
a. Use `cat`, `head`, and `tail` with pipes to display only lines 3-5 of your `sample.fasta` file. (Hint: `head -n 5 | tail -n 3`)
b. Count how many lines in the `yeast_mbp1.fasta` file contain the sequence motif 'CGC' (case-sensitive). (Hint: Use `grep` and `wc -l`). Remember `grep` finds the pattern anywhere on the line.

---

### Part 5: Searching and Filtering Text (`grep`)

`grep` (Global Regular Expression Print) searches for patterns (text strings or regular expressions) in files or input streams.

**Key Options:**
* `grep <pattern> <filename>`: Find pattern in file.
* `grep -i <pattern> <filename>`: **I**gnore case during search.
* `grep -v <pattern> <filename>`: In**v**ert match (show lines that *don't* match the pattern).
* `grep -c <pattern> <filename>`: **C**ount matching lines (shortcut for `grep ... | wc -l`).
* `grep -n <pattern> <filename>`: Show line **n**umbers along with matching lines.
* `grep -E <regex_pattern> <filename>`: Use **E**xtended regular expressions (more powerful patterns).
* `grep '^pattern'` : Find lines *starting* with the pattern (`^`).
* `grep 'pattern$'`: Find lines *ending* with the pattern (`$`).

```bash
# In raw_data/sample.fasta:
# Find sequences containing "GATTACA"
grep "GATTACA" sample.fasta

# Find sequence headers (lines starting with '>')
grep "^>" sample.fasta
# Count them directly
grep -c "^>" sample.fasta

# Find lines that are NOT sequence headers (i.e., the sequence lines)
grep -v "^>" sample.fasta

# Find headers containing "OrganismA"
grep "^>" sample.fasta | grep "OrganismA"

# Find headers for GeneY or GeneZ (using Extended Regex)
grep -E 'GeneY|GeneZ' sample.fasta | grep "^>"
```

**Exercise 5:**
a. In `reference_genomes/human_insulin.fasta`, find the line containing the organism name (Hint: Search for `OS=`). Use the `-n` option to see the line number.
b. Count how many sequence lines (lines *not* starting with `>`) are in `raw_data/yeast_mbp1.fasta`. Use `grep -v` and `grep -c`.
c. Display the header line(s) in `raw_data/sample.fasta` that contain `GeneX`.

---

### Part 6: Text Manipulation (`sed` and `awk`)

These are powerful stream editors for modifying text data. They are often used in bioinformatics pipelines to reformat files.

1.  **`sed` (Stream Editor):** Good for simple substitutions, deletions, or printing specific lines based on patterns. Works line by line.
    * **Basic Substitution:** `sed 's/<find_pattern>/<replace_pattern>/g' <filename>`
        * `s`: Substitute command.
        * `/`: Delimiter (can be other characters like `#` or `|`).
        * `g`: **G**lobal replacement (replace all occurrences on a line, not just the first). Omit `g` to replace only the first match per line.
    * **Deleting lines:** `sed '/<pattern_to_match>/d' <filename>`
    * **Acting on specific lines:** `sed '/<pattern_to_match>/ s/<find>/<replace>/g' <filename>` (only performs substitution on lines matching the initial pattern).

    ```bash
    cd ~/project_alpha/raw_data

    # Display sample.fasta, replacing all 'A' with 'T' (doesn't change the file)
    sed 's/A/T/g' sample.fasta

    # Replace spaces in sequence headers with underscores ONLY on header lines
    # We use a different delimiter '#' because the pattern contains '/'
    sed '/^>/ s#_Organism#|Organism#' sample.fasta # Replace first _ with | on headers

    # Delete header lines (just display sequence)
    sed '/^>/d' sample.fasta

    # To save the changes, redirect output to a new file:
    sed '/^>/ s/_/|/' sample.fasta > sample_header_mod.fasta
    cat sample_header_mod.fasta
    ```

2.  **`awk`:** A versatile pattern-scanning and processing language. Excellent for field-based operations (columns). By default, `awk` splits lines into fields based on whitespace (spaces or tabs). Fields are accessed using `$1`, `$2`, `$3`, etc. `$0` represents the entire line.
    * **Syntax:** `awk '<condition> { <action> }' <filename>`
    * The `<condition>` is optional (if omitted, action applies to all lines).
    * The `{ <action> }` block contains commands, often `print`.
    * `-F<delimiter>`: Specify a field separator (e.g., `-F','` for CSV, `-F'\t'` for TSV).

    ```bash
    # Create a simple tab-separated file (e.g., gene counts)
    echo -e "GeneID\tCount1\tCount2" > ../results/counts.tsv # -e enables interpretation of \t (tab)
    echo -e "GeneA\t100\t50" >> ../results/counts.tsv
    echo -e "GeneB\t200\t75" >> ../results/counts.tsv
    echo -e "GeneC\t50\t25" >> ../results/counts.tsv
    cat ../results/counts.tsv

    # Print only the first column (GeneID) from counts.tsv
    awk '{ print $1 }' ../results/counts.tsv

    # Print GeneID (col 1) and Count2 (col 3)
    awk '{ print $1, $3 }' ../results/counts.tsv

    # Print GeneID and sum of counts (field 2 + field 3) for lines where Count1 > 60
    # NR > 1 skips the header row (Record Number > 1)
    awk 'NR > 1 && $2 > 60 { print $1, $2 + $3 }' ../results/counts.tsv

    # Extract just the sequence ID from sample.fasta headers (remove '>')
    # Pipe grep output to awk. Set '>' as Field Separator, print 2nd field.
    grep "^>" sample.fasta | awk -F'>' '{ print $2 }'
    ```

**Exercise 6:**
a. Use `sed` to display the `reference_genomes/human_insulin.fasta` content, but remove the `(Homo sapiens)` part including the parentheses. (Hint: `sed 's/(Homo sapiens)//'`).
b. Use `awk` on the `results/counts.tsv` file to print only the gene names (first column), skipping the header line. (Hint: Use `NR > 1`).
c. Use `awk` on `results/counts.tsv` to print the GeneID and Count1, but only for genes where Count2 is less than or equal to 50 (skip the header).

---

### Part 7: Scripting Basics (Loops, Conditionals, Reading Files)

You can combine commands into script files (usually ending in `.sh`) to automate tasks. A script typically starts with `#!/bin/bash` (called a "shebang") to specify that Bash should execute it.

1.  **`for` loop:** Iterates over a list of items (like filenames).
    ```bash
    # Create a script file in project_alpha/scripts
    cd ~/project_alpha/scripts
    # Use a text editor like 'nano' or 'vim' to create the file:
    # nano process_fastas.sh

    # --- Start of process_fastas.sh ---
    #!/bin/bash

    echo "Processing FASTA files in ../raw_data/"

    # Loop through all files ending in .fasta in the raw_data directory
    for fasta_file in ../raw_data/*.fasta
    do
      echo "--- Processing $fasta_file ---"

      # Get the base filename without the path
      base_name=$(basename "$fasta_file")

      echo "Counting sequences in $base_name:"
      grep -c "^>" "$fasta_file"

      echo "Extracting headers from $base_name:"
      grep "^>" "$fasta_file" | sed 's/>//' # Remove '>'

      echo "" # Add a blank line for readability
    done

    echo "--- Processing complete. ---"
    # --- End of process_fastas.sh ---

    # Save and exit the editor (e.g., Ctrl+X, then Y, then Enter in nano)

    # Make the script executable
    chmod +x process_fastas.sh

    # Run the script (use ./ to run from current directory)
    ./process_fastas.sh
    ```
    * `"$fasta_file"`: Always quote variables containing filenames to handle spaces or special characters correctly.
    * `$(command)`: Command substitution - runs the command and substitutes its output.

2.  **`if-else` conditional:** Executes commands based on whether a condition is true or false.
    * **Syntax:**
        ```bash
        if [ <condition> ]; then
          # commands if condition is true
        elif [ <another_condition> ]; then
          # commands if another_condition is true
        else
          # commands if all conditions are false
        fi
        ```
    * **Common Conditions:**
        * `-f <file>`: True if `file` exists and is a regular file.
        * `-d <dir>`: True if `dir` exists and is a directory.
        * `-z "$var"`: True if variable `var` is empty (zero length).
        * `-n "$var"`: True if variable `var` is not empty.
        * `"$var1" == "$var2"`: True if strings are equal.
        * `"$var1" != "$var2"`: True if strings are not equal.
        * `N1 -eq N2` (equal), `-ne` (not equal), `-gt` (greater than), `-ge` (greater or equal), `-lt` (less than), `-le` (less or equal) for numerical comparisons.

    ```bash
    # --- Example script: check_file.sh ---
    #!/bin/bash

    FILENAME="../reference_genomes/human_insulin.fasta"

    echo "Checking for file: $FILENAME"

    if [ -f "$FILENAME" ]; then
      echo "File exists."
      # Check if it's empty
      if [ -s "$FILENAME" ]; then # -s checks if file size is greater than zero
         echo "File is not empty. Header:"
         head -n 1 "$FILENAME"
      else
         echo "File exists BUT IS EMPTY."
      fi
    else
      echo "ERROR: File not found."
    fi
    # --- End of check_file.sh ---

    # chmod +x check_file.sh
    # ./check_file.sh
    ```

3.  **Reading a file line by line (`while IFS= read -r line`)**: The standard, safe way to process a file's content line by line within a script.
    ```bash
    # Create a file with sample IDs: sample_list.txt in results dir
    echo "Sample_A01" > ../results/sample_list.txt
    echo "Sample_B05" >> ../results/sample_list.txt
    echo "Sample_C12" >> ../results/sample_list.txt

    # --- Example script: run_analysis_per_sample.sh ---
    #!/bin/bash

    INPUT_LIST="../results/sample_list.txt"

    if [ ! -f "$INPUT_LIST" ]; then
      echo "Error: Sample list $INPUT_LIST not found."
      exit 1 # Exit script with an error status
    fi

    echo "Starting analysis based on $INPUT_LIST"

    while IFS= read -r sample_id || [[ -n "$sample_id" ]]; do
      # Skip empty lines or lines starting with # (comments)
      if [[ -z "$sample_id" || "$sample_id" == \#* ]]; then
          continue # Skip to next iteration
      fi

      echo "  Processing Sample ID: $sample_id"
      # Imagine running a bioinformatics tool here, e.g.:
      # echo "  Running alignment for $sample_id..."
      # bwa mem reference.fasta ../raw_data/${sample_id}_R1.fastq.gz ../raw_data/${sample_id}_R2.fastq.gz > ../results/${sample_id}.sam
      sleep 0.5 # Simulate work
    done < "$INPUT_LIST" # Redirect file content into the while loop's input

    echo "Finished processing all samples."
    # --- End of run_analysis_per_sample.sh ---

    # chmod +x run_analysis_per_sample.sh
    # ./run_analysis_per_sample.sh
    ```
    * `IFS=`: Prevents trimming leading/trailing whitespace from lines.
    * `read -r`: Prevents backslash interpretation (raw read).
    * `|| [[ -n "$sample_id" ]]`: Handles the case where the last line in the file doesn't end with a newline character.
    * `< "$INPUT_LIST"`: Redirects the content of the file to the standard input of the `while` loop.

**Exercise 7:**
a. Create a script named `check_data.sh` in the `scripts` directory.
b. Inside the script, use a `for` loop to iterate through the files `../raw_data/sample.fasta` and `../raw_data/yeast_mbp1.fasta`.
c. Inside the loop, use an `if` statement (`if [ -f "$filename" ]`) to check if the file exists.
d. If it exists, print a message like "`<filename>` exists, number of lines: `N`", where `N` is the line count obtained using `wc -l`. (Hint: Use command substitution `$(wc -l < "$filename" | awk '{print $1}')` to get just the number).
e. If it doesn't exist, print an error message like "ERROR: `<filename>` not found."
f. Make the script executable and run it.

---

### Part 8: Environment Variables & Configuration (`.bashrc`)

**Environment Variables:** Variables that store information about your shell session and operating system environment. They are often used by programs to find necessary files or settings. Conventionally, they are named in uppercase.
* `echo $VARNAME`: Displays the value of a variable (e.g., `echo $HOME`, `echo $USER`, `echo $PATH`).
* `export VARNAME="value"`: Sets an environment variable for the current shell session and any programs or scripts started *from* that session.

```bash
# See your home directory path
echo $HOME

# See your username
echo $USER

# See the PATH: a colon-separated list of directories where the shell looks for commands
echo $PATH

# Temporarily add your project's script directory to the PATH for this session
# (This means you could run your scripts from anywhere without typing ./ or the full path)
export PATH="$PATH:$HOME/project_alpha/scripts"
echo $PATH # See the updated path

# Now try running a script from your home directory (cd ~)
# check_data.sh # It should run if the PATH was set correctly

# Note: This change is only for the current terminal session.
```

**`.bashrc` file:** A hidden configuration script in your home directory (`~/.bashrc`). It runs automatically every time you start a *new* interactive Bash shell (e.g., open a new terminal window). Use it to:
* Set environment variables permanently (like adding custom directories to `$PATH`).
* Create *aliases* (shortcuts for longer commands).
* Customize your shell prompt (`$PS1`).

```bash
# Edit the file (use nano or another editor)
# nano ~/.bashrc

# --- Add lines like these to the END of ~/.bashrc ---

# Add my project scripts directory to the PATH permanently
# export PATH="$PATH:$HOME/project_alpha/scripts"

# Create an alias 'll' for 'ls -lh' (a common useful alias)
# alias ll='ls -lh'

# Create a bioinformatics alias: count sequences in a fasta file
# alias countfasta='grep -c "^>"'

# --- Save and exit the editor ---

# To apply the changes to your CURRENT shell session, run:
source ~/.bashrc
# Alternatively, just open a new terminal window.

# Now test your aliases:
ll # Should run ls -lh
countfasta ../raw_data/sample.fasta # Should output 3
```

**Exercise 8:**
a. Use `echo` to view the value of your `$SHELL` environment variable (shows your default shell).
b. Edit your `~/.bashrc` file and add an alias: `alias projectdir='cd ~/project_alpha'`.
c. Run `source ~/.bashrc`.
d. Go to your root directory (`cd /`).
e. Type `projectdir` and press Enter. Use `pwd` to verify that the alias took you to the `~/project_alpha` directory.

---

**Conclusion**

You've now covered the fundamentals of the Unix/Bash command line, including navigation, file management, downloading, the power of piping, text processing with `grep`, `sed`, and `awk`, basic scripting constructs, and environment configuration. These are essential skills for tackling bioinformatics analyses efficiently and reproducibly.

**Key Takeaways:**
* The command line is powerful for handling large data and automating tasks.
* Mastering `cd`, `ls`, `cp`, `mv`, `rm` is crucial for file management (be careful with `rm`!).
* `wget` is your tool for downloading data.
* Piping (`|`) lets you build complex workflows from simple tools.
* `grep`, `sed`, and `awk` are indispensable for searching and modifying text files (like FASTA, GFF, VCF).
* Shell scripting (`for`, `if`, `while`) automates your analyses.
* `.bashrc` helps customize your environment and create shortcuts (aliases).

**Practice is key!** Try applying these commands to other sample files or exploring the options (`man <command>` or `<command> --help`) for the tools you've learned. Good luck!

