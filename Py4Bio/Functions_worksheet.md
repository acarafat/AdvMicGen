# 🧪 Introduction to Functions in Python

---

## ⏱️ Part 1: Basic Concepts

### 1.1 What is a Function?
A function is a block of code that performs a specific task. It helps in making the code reusable and more organized.

**Function Syntax:**
```python
def function_name(parameters):
    # Function body
    return result
```

**🌬️ Example 1: Population Growth Rate**

The formula is:
\[
\text{growth rate} = \frac{\text{population at time } t - \text{population at time } t_0}{\text{time difference}}
\]

```python
def calculate_growth_rate(population_t, population_t0, time_diff):
    growth_rate = (population_t - population_t0) / time_diff
    return growth_rate
```

**Test:**
```python
calculate_growth_rate(1500, 1000, 5)
```

---

### 1.2 Functions with Multiple Parameters

```python
def calculate_growth_rate(initial_population, final_population, time_diff):
    growth_rate = (final_population - initial_population) / time_diff
    return growth_rate
```

**Test:**
```python
calculate_growth_rate(1000, 5000, 10)
```

---

### 1.3 Using Return Values

Modify the function to interpret the result:

```python
def calculate_growth_rate(initial_population, final_population, time_diff):
    growth_rate = (final_population - initial_population) / time_diff
    if growth_rate > 50:
        return "Rapid growth", growth_rate
    elif growth_rate > 0:
        return "Slow growth", growth_rate
    else:
        return "No growth or decline", growth_rate
```

---

## ⏱️ Part 2: Intermediate Concepts 

### 2.1 Default Arguments

```python
def calculate_growth_rate(initial_population, final_population, time_diff=1):
    growth_rate = (final_population - initial_population) / time_diff
    return growth_rate
```

**Test:**
```python
calculate_growth_rate(1000, 5000)
```

---

### 2.2 DNA Sequence GC Content

```python
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    gc_content = (gc_count / len(dna_sequence)) * 100
    return gc_content
```

**Test:**
```python
calculate_gc_content("AGCTGCATG")
```

---

### 2.3 Multiple Return Values

```python
def calculate_gc_content(dna_sequence):
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    gc_content = ((g_count + c_count) / len(dna_sequence)) * 100
    return g_count, c_count, gc_content
```

**Test:**
```python
calculate_gc_content("AGCTGCATG")
```

---

## ⏱️ Part 3: Advanced Concepts

### 3.1 Lambda Functions, aka one-liner functions

```python
gc_content = lambda dna: ((dna.count("G") + dna.count("C")) / len(dna)) * 100
```

**Test:**
```python
gc_content("AGCTGCATG")
```

---

### 3.2 Recursion: Factorial Function

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

**Test:**
```python
factorial(5)
```

---

### 3.3 Biochemical Reaction Rate

Using the Law of Mass Action:
\[
\text{Rate} = k \times [A] \times [B]
\]

```python
def rate_of_reaction(k, concentration_A, concentration_B):
    return k * concentration_A * concentration_B
```

**Test:**
```python
rate_of_reaction(0.5, 2, 3)
```

---

## 💡 Bonus Challenge

### DNA Sequence Similarity

Write a function to calculate percent similarity between two DNA sequences based on matching characters at the same positions.

```python
def sequence_similarity(seq1, seq2):
    min_len = min(len(seq1), len(seq2))
    match_count = 0
    for i in range(min_len):
        if seq1[i] == seq2[i]:
            match_count += 1
    return (match_count / min_len) * 100
```

**Test:**
```python
sequence_similarity("AGCT", "AGGT")
```

---



