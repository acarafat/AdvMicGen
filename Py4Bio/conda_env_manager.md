# Bioinformatics Software Management with Miniconda and Mamba

## What is Miniconda?
Miniconda is a minimal installer for Conda. Conda is an open-source package management system and environment management system. Think of it as a tool that helps you install software packages and manage different sets of software for different projects without them interfering with each other.

Unlike Anaconda, which comes bundled with a large number of packages, Miniconda includes only Conda, Python, and a few essential dependencies. This makes Miniconda lightweight and flexible, allowing you to install only the packages you need for your specific tasks.

### Why use Conda (and Miniconda) in Bioinformatics?

Bioinformatics often involves using a wide variety of tools, each with its own dependencies (specific versions of programming languages, libraries, and other software). Manually installing and managing these dependencies can be challenging and lead to conflicts. Conda simplifies this by:

**Package Management**: Easily installing bioinformatics software and their required libraries.

**Dependency Resolution**: Automatically figuring out and installing all the necessary dependencies for a given package, resolving potential conflicts between different software requirements.

**Environment Management**: Creating isolated environments for different projects or tools, ensuring that the dependencies for one project do not interfere with another.

## Speeding up Conda with Mamba
While Conda is powerful, the dependency resolution process can sometimes be slow, especially with complex environments and many packages. Mamba is a re-implementation of Conda's package manager in C++. It offers significantly faster dependency resolution and package downloading, making your workflow more efficient.

Mamba can be used as a drop-in replacement for most conda commands. Many users install mamba into their base Conda environment or use Mambaforge, a distribution that includes Mamba by default. The conda-libmamba-solver is also now integrated into Conda, allowing Conda to use the faster libmamba backend for solving environments.

### How to use Mamba for faster operations:

Once Mamba is installed or if you are using a distribution like Mambaforge, you can simply replace conda with mamba in your commands for faster execution. For example, instead of conda install ..., you would use mamba install ....

If you are using a recent version of Conda, you might already be using the conda-libmamba-solver by default or can enable it.

## The Importance of Separate Conda Environments in Bioinformatics
In bioinformatics, you'll likely work on different projects that may require different versions of the same software or entirely different sets of tools. Installing all these tools in a single, central location can lead to "dependency hell," where the requirements of one tool conflict with another.

Separate environments solve this by:

**Isolation**: Each environment is an isolated directory containing specific versions of Python, R, and other packages.

**Reproducibility**: You can easily export the list of packages and their versions in an environment, allowing you to recreate the exact same software setup on another machine. This is crucial for reproducible research.

**Project-Specific Dependencies**: You can tailor environments to the specific needs of each project, avoiding unnecessary software clutter.

**Avoiding Conflicts**: Different versions of the same library or tool can coexist in different environments without causing issues.

## Example Scenario:

Imagine you are working on two bioinformatics projects:

**Project A** requires an older version of a genome aligner (e.g., bowtie2 version 2.2.4) and a specific version of Python (e.g., Python 3.7).

**Project B** requires the latest version of a different aligner (e.g., bwa version 0.7.17) and a newer version of Python (e.g., Python 3.9).

Without separate environments, installing these conflicting requirements would be difficult or impossible. With Conda environments, you can create a dedicated environment for Project A with its specific dependencies and another environment for Project B with its dependencies.

## Managing Conda Environments: A Practical Guide
Here are the essential commands for managing your Conda environments.

1. Creating a New Environment:

To create a new environment, you use the conda create or mamba create command followed by the environment name and the packages you want to install initially.

```bash
conda create --name my_bioinfo_env python=3.8
# Or using mamba for potentially faster creation:
# mamba create --name my_bioinfo_env python=3.8
```

`--name my_bioinfo_env`: Assigns the name my_bioinfo_env to your new environment. Choose a descriptive name related to your project or tools.

`python=3.8`: Specifies that you want Python version 3.8 installed in this environment. You can specify other package versions or add more packages directly during creation.

Example: Creating an environment for a specific tool

Let's create an environment specifically for using the popular bioinformatics tool fastqc. We'll also specify a Python version, as many bioinformatics tools have Python dependencies. We'll install fastqc and multiqc from the bioconda channel, which is a popular channel for bioinformatics packages.

```bash
conda create --name fastqc_env python=3.9 fastqc multiqc -c bioconda -c conda-forge
# Or with mamba:
# mamba create --name fastqc_env python=3.9 fastqc multiqc -c bioconda -c conda-forge
```

`-c bioconda`: Specifies the bioconda channel to search for packages.

`-c conda-forge`: Specifies the conda-forge channel, another important community-driven channel. It's good practice to include both when working with bioinformatics tools.

2. Activating an Environment:

Before you can use the packages installed in an environment, you need to activate it.

```bash
conda activate fastqc_env
# Or with mamba:
# mamba activate fastqc_env
```

Once activated, your terminal prompt will usually show the name of the active environment (e.g., (fastqc_env) ваш_пользователь@ваш_компьютер:~/$). Now, any commands you run will use the software installed within this environment.

3. Installing Packages into an Environment:

With an environment activated, you can install additional packages using conda install or mamba install.

```bash
conda install samtools bowtie2 -c bioconda -c conda-forge
# Or with mamba:
# mamba install samtools bowtie2 -c bioconda -c conda-forge
```

This will install samtools and bowtie2 into the currently active environment, pulling packages from the bioconda and conda-forge channels.

Example: Installing a specific version of a package

You can also specify the version of a package to install.

```bash
conda install blast=2.11.0 -c bioconda
# Or with mamba:
# mamba install blast=2.11.0 -c bioconda
```

This will install version 2.11.0 of the BLAST tool.

4. Listing Installed Packages in an Environment:

To see which packages are installed in your current environment, use conda list.

```bash
conda list
```

This will show a list of all packages and their versions within the active environment.

5. Deactivating an Environment:

When you're done working in an environment, you should deactivate it to return to your base environment or the system's default Python.

```bash
conda deactivate
```

The environment name should disappear from your terminal prompt.

6. Listing All Your Environments:

To see a list of all the Conda environments you have created, use conda env list or conda info --envs.

```bash
conda env list
# Or:
# conda info --envs
```

This will show the names and locations of all your environments. The active environment will be indicated by an asterisk (*).

7. Removing an Environment:

If you no longer need an environment, you can remove it. Be careful with this command as it will delete the environment and all packages within it.

```bash
conda env remove --name fastqc_env
# Or:
# mamba env remove --name fastqc_env
```
You will be asked to confirm the removal.

Worksheet Exercises:
**Install Miniconda:** If you haven't already, download and install Miniconda from the official website. Follow the installation instructions for your operating system.

**Verify Installation:** Open a new terminal or command prompt and type `conda --version`. You should see the installed Conda version.

**Create an Environment for RNA Sequencing Analysis:** Create a new Conda environment named rnaseq_env with Python 3.9.

```bash
conda create --name rnaseq_env python=3.9

# or using mamba:

mamba create --name rnaseq_env python=3.9
```

Activate the RNA Sequencing Environment: Activate the rnaseq_env.

```bash
conda activate rnaseq_env

#or using mamba:

mamba activate rnaseq_env
```

Install RNA Sequencing Tools: Install the following tools into the rnaseq_env from the bioconda and conda-forge channels: fastp, hisat2, samtools, stringtie.

```bash
conda install fastp hisat2 samtools stringtie -c bioconda -c conda-forge

#or using mamba:

mamba install fastp hisat2 samtools stringtie -c bioconda -c conda-forge
```

Observe the difference in speed if you compare conda install and mamba install for a similar set of packages in a new environment.

List Installed Packages: List the packages installed in the rnaseq_env.

```bash
conda list
```

Deactivate the Environment: Deactivate the rnaseq_env.

```bash
conda deactivate
```

Create an Environment for Variant Calling: Create another environment named variant_calling_env with Python 3.8 and install bwa and bcftools from the bioconda channel.

```bash
conda create --name variant_calling_env python=3.8 bwa bcftools -c bioconda -c conda-forge

#or using mamba:

mamba create --name variant_calling_env python=3.8 bwa bcftools -c bioconda -c conda-forge
```

List All Your Environments: See the list of all your created environments.

conda env list

(Optional) Remove an Environment: If you wish, remove the rnaseq_env.

```bash
conda env remove --name rnaseq_env

#or using mamba:

mamba env remove --name rnaseq_env
```

By completing this worksheet, you should have a good understanding of how to use Miniconda and Mamba to manage isolated environments for your bioinformatics work, leading to a more organized, reproducible, and efficient workflow.
