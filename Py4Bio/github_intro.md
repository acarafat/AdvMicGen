# Understanding and Using Git and GitHub: A Worksheet for Bioinformatics

This worksheet will introduce you to the essential concepts of Git and GitHub and explain why they are invaluable tools for bioinformatics researchers.

## Rationale: Why Git and GitHub?

Imagine you're working on a bioinformatics project. You have scripts for data processing, analysis, and visualization. You're constantly making changes, trying new approaches, and fixing errors. Without a system to track these changes, you can quickly end up with a confusing mess of files named `analysis_v1.R`, `analysis_final.R`, `analysis_final_ 진짜_final.R`, and so on. This is where version control comes in.

**Version Control Systems (VCS)** are tools that track changes to files over time. They allow you to:

* **Keep a history of every change:** See exactly what modifications were made, when, and by whom.

* **Revert to previous versions:** Easily go back to an earlier state of your project if something goes wrong.

* **Branch and merge:** Experiment with new ideas or features in isolation without affecting the main project, and then integrate those changes later.

* **Understand the evolution of your code:** See how your project has developed step by step.

**Git** is a powerful, distributed version control system. "Distributed" means that every user has a full copy of the project's history, allowing for offline work and robust collaboration.

**GitHub** is a web-based platform that provides hosting for Git repositories. While you can use Git alone, GitHub adds a layer of collaboration and project management features, including:

* **Remote storage:** A central place to store your project, providing backup and allowing multiple people to access and contribute.

* **Issue tracking:** Manage tasks, bugs, and feature requests.

* **Pull requests:** A mechanism for proposing changes and having them reviewed before merging them into the main project.

* **Collaboration tools:** Facilitate teamwork and communication among researchers.

**In Bioinformatics, Git and GitHub are crucial because:**

* **Reproducibility:** Track every step of your analysis pipeline, ensuring that your results can be reproduced exactly.

* **Collaboration:** Easily share code and collaborate with colleagues locally and internationally.

* **Open Science:** Share your code publicly to promote transparency and allow others to build upon your work.

* **Project Management:** Organize complex bioinformatics projects with numerous scripts, data files, and documentation.

* **Protection against data loss:** Your project history is backed up on GitHub's servers.

## Fundamentals of Git

Let's explore some fundamental Git concepts and commands.

### 1. Repositories

A **repository** (or repo) is the core of a Git project. It contains all the project files and the complete history of changes.

* **Local Repository:** The copy of the repository stored on your computer.

* **Remote Repository:** A copy of the repository hosted on a server, like GitHub.

**Command:** `git init`

* **What it does:** Initializes a new Git repository in the current directory. This creates a hidden `.git` folder that stores all the repository's history and metadata.

**Command:** `git clone [repository_url]`

* **What it does:** Creates a copy of a remote repository on your local machine.

### 2. The Three States

In Git, files in your local repository can be in one of three states:

* **Working Directory:** The files you are currently editing.
* **Staging Area (or Index):** A place where you prepare changes to be committed. You select which changes you want to include in the next commit.
* **Git Repository:** The history of your committed changes.

### 3. Committing Changes

A **commit** is a snapshot of your staged changes at a specific point in time. Each commit has a unique identifier (a hash) and a commit message describing the changes.

**Command:** `git status`

* **What it does:** Shows the current state of your working directory and staging area. It tells you which files have been modified, which are staged, and which are untracked.

**Command:** `git add [file_name]` or `git add .`

* **What it does:** Adds changes from the working directory to the staging area. `git add .` stages all changes in the current directory and its subdirectories.

**Command:** `git commit -m "Your descriptive commit message"`

* **What it does:** Records the staged changes as a new commit in the local repository. The `-m` flag allows you to provide a concise commit message directly.

### 4. Branching and Merging

**Branches** allow you to diverge from the main line of development to work on new features or bug fixes without affecting the stable version of your project. The default branch is typically called `main` or `master`.

**Command:** `git branch`

* **What it does:** Lists all local branches.

**Command:** `git branch [new_branch_name]`

* **What it does:** Creates a new branch.

**Command:** `git checkout [branch_name]`

* **What it does:** Switches to the specified branch.

**Command:** `git merge [branch_name]`

* **What it does:** Merges the changes from the specified branch into the current branch.

### 5. Working with Remotes (GitHub)

To collaborate and back up your work, you'll interact with a remote repository on GitHub.

**Command:** `git remote add origin [remote_repository_url]`

* **What it does:** Adds a remote repository (commonly named `origin`) to your local repository.

**Command:** `git push origin [branch_name]`

* **What it does:** Uploads your local commits to the remote repository.

**Command:** `git pull origin [branch_name]`

* **What it does:** Downloads changes from the remote repository to your local repository and automatically merges them.

## Bioinformatics Examples

Let's walk through some scenarios in bioinformatics where Git and GitHub are invaluable.

### Example 1: Tracking Changes in a Variant Calling Pipeline

You've written a Python script `variant_caller.py` to analyze genomic data and identify variants.

1.  **Initialize a Git repository:**
    ```bash
    cd my_bioinformatics_project
    git init
    ```

2.  **Add and commit the initial script:**
    ```bash
    git add variant_caller.py
    git commit -m "Add initial variant calling script"
    ```

3.  **You modify the script to improve filtering.**
    ```bash
    # Edit variant_caller.py
    git status # See the modified file
    git add variant_caller.py
    git commit -m "Improve variant filtering in variant_caller.py"
    ```

4.  **Later, you realize the old filtering method was better for a specific dataset. You can revert to the previous commit.**
    ```bash
    git log # Find the commit hash of the previous version
    git checkout [previous_commit_hash] variant_caller.py # Revert the specific file
    # Or to revert the entire project to that commit (use with caution!)
    # git reset --hard [previous_commit_hash]
    ```

### Example 2: Developing a New Analysis Module

You want to add a new module to your project for differential gene expression analysis, but you don't want to break your existing variant calling workflow.

1.  **Create a new branch for the new module:**
    ```bash
    git branch differential_expression
    git checkout differential_expression
    ```

2.  **Develop the new module on this branch:**
    ```bash
    # Create and edit differential_expression.R
    git add differential_expression.R
    git commit -m "Add initial differential expression analysis script"
    ```

3.  **Switch back to the main branch to work on something else:**
    ```bash
    git checkout main
    ```

4.  **Once the differential expression module is ready, merge it into the main branch:**
    ```bash
    git merge differential_expression
    ```

### Example 3: Collaborating with a Colleague on a Shared Script

You're working with a colleague on a script `align_reads.sh` for aligning sequencing reads.

1.  **Create a repository on GitHub and clone it:**
    * Create a new repository on github.com.
    * Clone the repository to your local machine.
        ```bash
        git clone [https://github.com/your_username/your_bioinformatics_project.git](https://github.com/your_username/your_bioinformatics_project.git)
        cd your_bioinformatics_project
        ```

2.  **Add and push the initial script:**
    ```bash
    git add align_reads.sh
    git commit -m "Add initial read alignment script"
    git push origin main # Push to the 'main' branch on the 'origin' remote
    ```

3.  **Your colleague clones the repository and makes changes.** They commit and push their changes.

4.  **You want to get their updates:**
    ```bash
    git pull origin main # Pull changes from the 'main' branch on the 'origin' remote
    ```

5.  **If you both edited the same part of the `align_reads.sh` file, you might encounter a merge conflict. Git will notify you, and you'll need to manually resolve the conflict by editing the file to combine both sets of changes.** After resolving, you'll add and commit the merged file.

### Example 4: Using GitHub for Project Management and Code Review

Your bioinformatics project is getting larger, and you need to track bugs and new features.

1.  **Use GitHub Issues:** Your colleague finds a bug in your variant calling script. They open an "Issue" on your GitHub repository describing the bug. You can track its progress and discuss solutions within the issue.

2.  **Use Pull Requests for Code Review:** You've finished developing the differential expression module on its branch. Instead of merging directly, you open a "Pull Request" on GitHub. This proposes merging your `differential_expression` branch into `main`. Your colleagues can review your code, suggest changes, and add comments before the changes are merged.

## Exercises

To practice your Git and GitHub skills, try the following exercises:

1.  **Local Repository Practice:**
    * Create a new directory for a mock bioinformatics project.
    * Initialize a Git repository in the directory.
    * Create a few dummy files (e.g., `script1.py`, `data.csv`, `notes.txt`).
    * Add and commit these files.
    * Modify one file, stage only that file, and commit.
    * Create a new branch, switch to it, make changes to another file, and commit on that branch.
    * Switch back to the main branch.
    * (Optional) Try merging the new branch into the main branch.

2.  **GitHub Practice:**
    * Create a free GitHub account.
    * Create a new public repository on GitHub.
    * Clone the empty repository to your local machine.
    * Copy the files from your local practice repository into the cloned directory.
    * Add and commit the files in the cloned repository.
    * Push your local commits to the remote GitHub repository.
    * Go to the GitHub website and view your files and commit history.

3.  **Collaboration Simulation (Optional, requires a partner):**
    * With a colleague, have one person create a repository on GitHub.
    * The other person forks the repository (creates their own copy on GitHub).
    * Both individuals clone their respective repositories.
    * Both make changes to different files, commit, and push to their own repositories.
    * Have the person who forked the repository create a pull request to the original repository.
    * Have the original repository owner review and merge the pull request.
    * Have the person who forked pull the changes from the original repository to sync their copy.

## Further Learning

This worksheet provides a basic introduction. To deepen your understanding, explore these resources:

* **Git Documentation:** The official Git documentation is comprehensive: [https://git-scm.com/doc](https://git-scm.com/doc)
* **GitHub Guides:** GitHub provides helpful guides and tutorials: [https://guides.github.com/](https://guides.github.com/)
* **Software Carpentry's Version Control with Git lesson:** An excellent hands-on introduction for researchers: [https://swcarpentry.github.io/git-novice/](https://swcarpentry.github.io/git-novice/)
* **Online courses (Coursera, Udacity, etc.):** Many platforms offer in-depth courses on Git and GitHub.

By mastering Git and GitHub, you'll significantly improve your efficiency, reproducibility, and collaboration in your bioinformatics work. Good luck!
