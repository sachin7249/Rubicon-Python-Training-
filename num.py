import numpy as np

print("=" * 50)
print("       NUMPY STUDENT MARKS ANALYZER")
print("=" * 50)
# ------------------------------------------------
# 1. CREATE ARRAY
# ------------------------------------------------

marks = np.array([78, 85, 62, 91, 55, 88, 73, 95, 68, 81])

print("\nOriginal Marks:")
print(marks)

# ------------------------------------------------
# 2. ARRAY PROPERTIES
# ------------------------------------------------

print("\n--- Array Properties ---")

print("Number of Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Total Elements:", marks.size)
print("Data Type:", marks.dtype)
print("Memory per Element:", marks.itemsize, "bytes")

# ------------------------------------------------
# 3. INDEXING
# ----------------------…
print("\n--- Indexing ---")

print("First Student:", marks[0])
print("Second Student:", marks[1])
print("Last Student:", marks[-1])

# ------------------------------------------------
# 4. SLICING
# ------------------------------------------------

print("\n--- Slicing ---")

print("First 5 Students:", marks[:5])
print("Last 5 Students:", marks[5:])
print("Students 3 to 7:", marks[2:7])

# ------------------------------------------------
# 5. VECTORIZED OPERATIONS
# ------------------------------------------------

print("\n--- Vectorized Operations ---")

bonus = 5

new_marks = marks + bonus

print("Original Marks:", marks)
print("After Adding Bonus:", new_marks)

# Percentage calculation
percentage = marks / 100 * 100

print("Percentage:", percentage)

# ------------------------------------------------
# 6. STATISTICS
# ------------------------------------------------

print("\n--- Statistics ---")

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))
