# 🧬 Python for Biologists – 1-Hour Crash Course Cheatsheet

## 🔢 Python as a Calculator

```python
# Basic arithmetic
5 + 2        # 7
9 - 4        # 5
3 * 4        # 12
10 / 3       # 3.33...
10 // 3      # 3 (integer division)
2 ** 4       # 16 (exponentiation)
17 % 5       # 2 (modulus)
```

### Biology Example

```python
dna_base_masses = {'A': 313.2, 'T': 304.2, 'G': 329.2, 'C': 289.2}
sequence = "ATGCGT"
mass = sum(dna_base_masses[base] for base in sequence)
print("DNA mass:", mass)
```

## 🖐 math Module

```python
import math
math.log10(2000000)  # Log10 of population
math.sqrt(36)        # Square root
```

## 🎲 random Module

```python
import random
# Random nucleotide choice
base = random.choice(["A", "T", "G", "C"])
print("Random base:", base)


# Generate a random 10-base DNA sequence
random_seq = ''.join(random.choices(["A", "T", "G", "C"], k=10))
print("Random DNA sequence:", random_seq)
```

## 🌟 Data Types

```python
count = 1500          # int
concentration = 0.3   # float
gene = "lacZ"         # str
is_expressed = True   # bool
```

Check type:

```python
print(type(gene))  # <class 'str'>
```

## ➕ Operators
```python
# Comparison operators
5 == 5      # True (equal)
5 != 3      # True (not equal)
10 > 3      # True (greater than)
10 >= 10    # True (greater than or equal)
2 < 5       # True (less than)
3 <= 3      # True (less than or equal)
```

### Integer vs. Float Example
```python
a = 3      # int
b = 3.0    # float
print(a == b)      # True (value equal)
print(type(a))     # <class 'int'>
print(type(b))     # <class 'float'>
```

### Division Example
```python
print(10 / 3)   # 3.333... (float division)
print(10 // 3)  # 3 (integer division)
```

## 🛦 Data Structures

### Lists

```python
genes = ["lacZ", "araC", "recA"]
genes.append("trpE")
print(genes[1])
```

### Dictionaries

```python
gene_lengths = {"lacZ": 1023, "araC": 876}
gene_lengths["recA"] = 1170
```

### Tuples and Sets

```python
codon = ("A", "T", "G")
unique_genes = set(["lacZ", "recA", "lacZ"])
```

## 🔀 Loops

### for loop

```python
for gene in genes:
    print("Gene:", gene)
```

### while loop

```python
count = 0
while count < 3:
    print("Cycle", count)
    count += 1
```

### range()

```python
for i in range(1, 4):
    print("Sample", i)
```

## ⚖️ Conditionals

```python
if expression_level > 2.0:
    print("Highly expressed")
elif expression_level > 1.0:
    print("Moderately expressed")
else:
    print("Low expression")
```

## 📂 File Handling

### Read FASTA

```python
with open("sequence.txt") as f:
    for line in f:
        if not line.startswith(">"):
            print(line.strip())
```

### Write to File

```python
with open("output.txt", "w") as f:
    f.write("Gene: lacZ\n")
```

## 📚 Functions and Keywords

### Define a Function

```python
def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq) * 100
```

### Common Keywords

- `def`, `return`
- `if`, `elif`, `else`
- `for`, `while`, `in`
- `import`, `with`, `as`
- `True`, `False`, `None`
- `break`, `continue`, `pass`

## 🔬 Mini Project: GC Content from FASTA

```python
def read_fasta(path):
    with open(path) as f:
        lines = f.readlines()
    return ''.join(line.strip() for line in lines if not line.startswith(">"))

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)

sequence = read_fasta("sequence.txt")
gc = gc_content(sequence)

with open("gc_output.txt", "w") as f:
    f.write(f"GC content: {gc}%\n")

print("GC content:", gc, "%")
```

## 🎓 Summary

- Basic math and `math` module
- Data types and structures
- Loops and conditionals
- File I/O
- Functions and common keywords

Happy coding! 🧬

