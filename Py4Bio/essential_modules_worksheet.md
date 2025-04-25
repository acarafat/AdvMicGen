# Biology Data Science with Python

This worksheet introduces **NumPy**, **Pandas**, **Matplotlib**, and **Seaborn** using examples from biological data. It is designed for beginners in Python data science with an interest in life sciences.

---

## 🔢 Part 1: NumPy - Numerical Computing in Biology

### Introduction to Arrays and Matrices

Biological data like gene expression, DNA microarray data, or mutation matrices can be efficiently represented with arrays.

NumPy provides several ways to generate ranges of numbers, which is especially useful for creating index vectors, time points, or synthetic biological data.

```python
# np.arange: generates evenly spaced values within a given interval
print(np.arange(0, 10, 2))  # [0 2 4 6 8]

# np.linspace: generates evenly spaced numbers over a specified interval
print(np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1.  ]

# np.logspace: logarithmically spaced values (useful in plotting growth rates or concentrations)
print(np.logspace(1, 3, num=4))  # [  10.  100. 1000.]

# Example: time points in a simulation
time_points = np.linspace(0, 24, num=25)  # hours from 0 to 24
print("Time points (hours):", time_points)
```


### Matrix Manipulation and Multiplication

NumPy is widely used to do linear algebra, i.e. matrix manipulation.
Matrix operations are central to many bioinformatics analyses, such as computing similarities, transformations, or modeling interactions.

```python
import numpy as np

# Gene expression matrix (rows = genes, columns = samples)
gene_expression = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.7, 3.1, 4.7, 1.5]
])
print("Shape:", gene_expression.shape)
print("Mean expression per gene:", np.mean(gene_expression, axis=1))
print("Max expression per sample:", np.max(gene_expression, axis=0))
```


```python
# Matrix multiplication: sample correlation via dot product
# Let's assume we want to project gene expression using a transformation matrix
transformation = np.array([
    [1.0, 0.5, 0.2, 0.1],
    [0.3, 1.2, 0.4, 0.2]
])
projected = np.dot(transformation, gene_expression.T)
print("Projected gene expressions:
", projected)

# Element-wise multiplication
scaled_expression = gene_expression * 2
print("Scaled expression:
", scaled_expression)

# Matrix addition
offset = np.ones_like(gene_expression) * 0.5
adjusted_expression = gene_expression + offset
print("Adjusted expression:
", adjusted_expression)

# Identity matrix and its role in preserving matrix shape
identity = np.eye(gene_expression.shape[1])
identity_mult = np.dot(gene_expression, identity)
print("Multiplication with identity matrix:
", identity_mult)
```



### Why NumPy is Faster

```python
import time

# Using lists (Python)
a = list(range(1000000))
b = list(range(1000000))
start = time.time()
c = [x + y for x, y in zip(a, b)]
print("Python list time:", time.time() - start)

# Using NumPy
a_np = np.arange(1000000)
b_np = np.arange(1000000)
start = time.time()
c_np = a_np + b_np
print("NumPy time:", time.time() - start)
```

### More Useful NumPy Operations

```python
# Transpose of a matrix
print(gene_expression.T)

# Boolean masking
print(gene_expression[gene_expression > 5])

# Summarization
print("Standard deviation per gene:", np.std(gene_expression, axis=1))

# Linear algebra
cov_matrix = np.cov(gene_expression.T)
print("Covariance matrix:", cov_matrix)
```

---

## 🔹 Part 2: Matplotlib - Visualizing Biological Data

### Basic Plots: Bar Chart

```python
import matplotlib.pyplot as plt

genes = ['GeneA', 'GeneB', 'GeneC']
expression = [5.1, 4.9, 6.7]

plt.bar(genes, expression, color='teal')
plt.title('Expression Levels in Sample1')
plt.xlabel('Gene')
plt.ylabel('Expression')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

### Adding Layers to Plots

```python
samples = ['Sample1', 'Sample2', 'Sample3']
geneA = [5.1, 5.3, 5.5]
geneB = [4.9, 5.0, 5.2]

plt.plot(samples, geneA, label='GeneA', marker='o', linestyle='-', color='green')
plt.plot(samples, geneB, label='GeneB', marker='s', linestyle='--', color='orange')
plt.title('Expression Over Samples')
plt.xlabel('Samples')
plt.ylabel('Expression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

### Other Plot Types

```python
# Pie chart
sizes = [40, 35, 25]
labels = ['Upregulated', 'Downregulated', 'Unchanged']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gene Expression Categories')
plt.axis('equal')
plt.show()

# Histogram
plt.hist(gene_expression.flatten(), bins=5, color='purple', edgecolor='black')
plt.title('Histogram of All Expression Values')
plt.xlabel('Expression Level')
plt.ylabel('Frequency')
plt.show()
```

---

## 📃 Part 3: Pandas - Managing Biological Data

Most of the time your biological sequence data will be accompanied by some kind of meta data, living in a spreadsheet. Pandas Dataframe is perfect for handling those data.

### Creating DataFrames

```python
import pandas as pd

data = {
    'Gene': ['GeneA', 'GeneB', 'GeneC'],
    'Sample1': [5.1, 4.9, 6.7],
    'Sample2': [5.3, 5.0, 6.9]
}
df = pd.DataFrame(data)
print(df)
```

However, it's unlikely that you have to manually type in the data. You should read the meta data from a spreadsheet/csv/tsv file.

```python
# Reading a DataFrame from a CSV file
# Suppose you have a file 'gene_expression.csv' with gene expression values
# Format:
# Gene,Sample1,Sample2
# GeneA,5.1,5.3
# GeneB,4.9,5.0
# GeneC,6.7,6.9

df_from_csv = pd.read_csv('gene_expression.csv')
print(df_from_csv)

# To read a file with tab-delimited format (common in biological data), use:
df_tab = pd.read_csv('expression_data.tsv', sep='	')

# For large CSVs, read only specific columns or rows:
df_subset = pd.read_csv('gene_expression.csv', usecols=['Gene', 'Sample1'], nrows=10)

# Setting the first column as index
df_indexed = pd.read_csv('gene_expression.csv', index_col=0)
```





### Indexing and Subsetting

Often we need to find specific samples, subset the dataframe by particular condition, etc. 

```python
# Access column
print(df['Sample1'])

# Conditional subset
print(df[df['Sample1'] > 5.0])

# Using loc and iloc
print(df.loc[0, 'Gene'])
print(df.iloc[1, 2])

# Setting index
df.set_index('Gene', inplace=True)
print(df)

# Resetting index
df.reset_index(inplace=True)
```

### Reshaping Data: Melt and Pivot

```python
melted = pd.melt(df, id_vars=['Gene'], var_name='Sample', value_name='Expression')
print(melted)

pivoted = melted.pivot(index='Gene', columns='Sample', values='Expression')
print(pivoted)
```

### Writing Data to CSV

Once you have transformed or cleaned your DataFrame, you may want to save it:

```python
# Save the melted DataFrame to a CSV file
melted.to_csv('melted_expression.csv', index=False)

# Save the pivoted DataFrame, keeping the index
pivoted.to_csv('pivoted_expression.csv')

# Save only selected columns
df[['Gene', 'Sample1']].to_csv('subset_expression.csv', index=False)
```

### More Useful Pandas Methods

```python
# Describe summary
print(df.describe())

# Correlation
print(df.corr())

# Group by example
grouped = melted.groupby('Sample').mean()
print(grouped)

# Sorting
print(df.sort_values(by='Sample1', ascending=False))

```

---



## 🔽️ Part 4: Seaborn - Advanced Visualization

### Why Seaborn?

- Integrates well with Pandas
- Prettier and more informative plots
- Statistical functionality built-in
- Themes and aesthetics for scientific publication

```python
import seaborn as sns
sns.set(style='whitegrid')
```

### Creating Plots from Pandas DataFrame

```python
sns.barplot(data=melted, x='Gene', y='Expression', hue='Sample', palette='muted')
plt.title('Gene Expression Comparison')
plt.show()
```

### Other Plot Types

```python
# Boxplot
sns.boxplot(data=melted, x='Gene', y='Expression', palette='pastel')
plt.title('Expression Distribution')
plt.show()

# Violin plot
sns.violinplot(data=melted, x='Gene', y='Expression', inner='point', palette='Set2')
plt.show()

# Scatterplot (without regression line)
sns.lmplot(data=melted, x='Gene', y='Expression', fit_reg=False)

# Heatmap
heatmap_data = pivoted.fillna(0)
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu')
plt.title('Expression Heatmap')
plt.show()
```

### Using Seaborn with Matplotlib

```python
plt.figure()
ax = sns.boxplot(data=melted, x='Gene', y='Expression')
ax.set_title('Gene Expression Boxplot')
ax.set_ylabel('Expression Level')
plt.grid(True)
plt.show()
```

---

## ✅ Exercises

1. Create a NumPy array for mutation frequencies in 10 genes across 3 populations. Use `np.random.randint()`.
2. Visualize this using a grouped bar chart. Label each group properly.
3. Convert this to a Pandas DataFrame, melt it, and use Seaborn to make a boxplot.
4. Apply filters and slicing on the DataFrame to show only high-frequency mutations (e.g., >10).
5. Combine Matplotlib and Seaborn to make a final styled plot with custom titles, labels, and colors.

---

This worksheet is designed to get you started with real biological data analysis in Python. Explore more by using real-world datasets like those from GEO, TCGA, or Ensembl!

