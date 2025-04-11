# 🧪 Python for Biologists – Worksheet

This worksheet is an extended, hands-on journey through Python basics for biologists. Designed for 1 hours of interactive learning with examples and exercises. Each block is followed by a small task or thought experiment.

---

## 🧮 1. Python as a Calculator

```python
5 + 2        # 7
9 - 4        # 5
3 * 4        # 12
10 / 3       # 3.33...
10 // 3      # 3 (integer division)
2 ** 4       # 16
17 % 5       # 2
```

### Common Math Operations

- `+`: addition
- `-`: subtraction
- `*`: multiplication
- `/`: float division
- `//`: integer division
- `%`: modulo (remainder)
- `**`: exponentiation

**🧪 Task:** Calculate molecular weight of a DNA strand using `sum()` and dictionary lookup.

```python
dna_base_masses = {'A': 313.2, 'T': 304.2, 'G': 329.2, 'C': 289.2}
sequence = "ATGCGT"
mass = sum(dna_base_masses[base] for base in sequence)
print("DNA mass:", mass)
```

---

## 🖐️ 2. math Module

```python
import math
print(math.log10(2000000))  # Log10 of population
print(math.sqrt(36))        # Square root
print(math.exp(2))          # Exponential
```

### Common Functions in `math`

- `math.sqrt(x)`: square root
- `math.exp(x)`: e^x
- `math.log(x, base)`: logarithm with custom base (base 10 = `math.log10()`)
- `math.pi`: π constant

**🧪 Task:** Use `math.log()` with different bases (e.g., natural log).

---

## 🎲 3. random Module

```python
import random
print(random.choice(["A", "T", "G", "C"]))
print(''.join(random.choices(["A", "T", "G", "C"], k=10)))
```

### Useful `random` Methods & Examples

- `random.random()`: random float [0.0, 1.0)
- `random.randint(a, b)`: random int between a and b
- `random.choice(list)`: pick one item
- `random.choices(list, k=n)`: pick n items with replacement
- `random.shuffle(list)`: shuffle in-place

**🧪 Task:** Generate a 50-base random DNA sequence.

---

## 🌟 4. Data Types and Formatting

Python has several built-in data types. Here are the most commonly used ones:

### Integers (`int`)
Whole numbers without a decimal point.
```python
a = 42
print(type(a))  # <class 'int'>
```
**Useful `int` methods/functions:**
```python
print(bin(10))  # '0b1010' (binary)
print(int("1010"))  # Convert string to integer
```

### Floating-point numbers (`float`)
Numbers with decimal points.
```python
b = 3.14
print(type(b))  # <class 'float'>
```
**Methods/Functions:**
```python
print(round(3.14159, 2))  # 3.14
print(float("3.5"))  # Convert string to float
```

### Strings (`str`)
Text or characters inside quotes.
```python
name = "lacZ"
print(type(name))  # <class 'str'>
```
**Useful `str` methods:**
```python
print(name.upper())   # 'LACZ'
print(name.lower())   # 'lacz'
print(name.startswith("la"))  # True
print(name.replace("Z", "Y"))  # 'lacY'
```

### String Formatting Examples
```python
gene = "trpE"
expr = 8.4567
print(f"{gene} expression: {expr:.2f}")
print("%s expression: %.2f" % (gene, expr))
```

### Comparing Data Types
```python
a = 3
b = 3.0
print(a == b)              # True (same value)
print(type(a), type(b))    # <class 'int'> <class 'float'>
```

### Integer Division vs Float Division
```python
print(10 / 3)   # 3.3333 (float division)
print(10 // 3)  # 3 (integer division)
```

**🧪 Task:** Format expression level to two decimal places using both f-string and %% formatting. Try converting a float string to a number.

```python
name = "lacZ"
length = 1023
print(f"Gene {name} is {length} bp long")
print("Gene %s is %d bp long" % (name, length))
```

```python
a = 3
b = 3.0
print(a == b)              # True in value
print(type(a), type(b))    # int vs float
```

### String Formatting Examples

```python
gene = "trpE"
expr = 8.4567
print(f"{gene} expression: {expr:.2f}")
print("%s expression: %.2f" % (gene, expr))
```

**🧪 Task:** Format expression level to two decimal places using f-string.

---

## ➗ 5. Operators and Comparisons

```python
5 == 5       # True
5 != 3       # True
10 > 3       # True
10 >= 10     # True
2 < 5        # True
3 <= 3       # True
```

```python
print(10 / 3)   # 3.3333 (float division)
print(10 // 3)  # 3 (integer division)
```

### Operator Types & Examples

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`

```python
expr = 2.5
if expr >= 2 and expr <= 10:
    print("Valid expression range")
```

**🧪 Task:** Write a condition to check if a GC% is above 50.

---

## 📃 6. Data Structures

### Lists

```python
genes = ["lacZ", "araC", "recA"]
genes.append("trpE")
print(genes[1])
```

#### Useful List Methods & Examples

```python
genes.remove("recA")
print(genes)
print(len(genes))
print(sorted(genes))
```

### Dictionaries

```python
expression = {"lacZ": 5.2, "araC": 2.9}
print(expression["lacZ"])
expression["recA"] = 4.7
```

#### Useful Dictionary Methods

```python
print(expression.keys())
print(expression.values())
print(expression.items())
```

### Tuples

```python
coords = (5, 10)
print(coords[0])
```

---

## 🔁 7. Loops

### For Loops

```python
dna = "ATGCGT"
for base in dna:
    print(base)
```

```python
genes = ["lacZ", "araC", "recA"]
for gene in genes:
    print(gene.upper())
```

### List Comprehension (One-liner loop)

A compact way to generate or transform lists.

```python
# Get lengths of all sequences in a list
sequences = ["ATGC", "GGTACC", "T"]
lengths = [len(seq) for seq in sequences]
print(lengths)  # [4, 6, 1]
```

```python
# Convert all gene names to lowercase
genes = ["LACZ", "ARAC", "RECA"]
lowercase_genes = [gene.lower() for gene in genes]
print(lowercase_genes)
```

### While Loops

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**🧪 Task:** Iterate through a list of DNA sequences and print their lengths.

---

## ❓ 8. Conditionals

```python
expression = 4.5
if expression > 5:
    print("Highly expressed")
elif expression > 2:
    print("Moderately expressed")
else:
    print("Low expression")
```

---

## 📂 9. File Handling

### Writing

```python
with open("genes.txt", "w") as file:
    file.write("lacZ\naraC\nrecA")
```

### Reading

```python
with open("genes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

**🧪 Task:** Write a FASTA header and sequence to a file.

---

## 🔍 10. Frequently Used Keywords

### Keywords to Recognize

- `if`, `else`, `elif`
- `for`, `while`, `break`, `continue`
- `def`, `return`
- `import`, `as`, `from`
- `with`, `open`, `in`, `not`, `and`, `or`, `is`
- `True`, `False`, `None`, `class`, `try`, `except`

---



