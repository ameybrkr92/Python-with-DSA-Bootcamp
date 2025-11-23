# 🚀 DSA + Python Complexity Master Revision Document

This is a complete, structured, easy‑to‑revise guide covering:
- Time Complexity
- Space Complexity
- Big‑O, Big‑Θ, Big‑Ω
- Best/Average/Worst case
- All common Big‑O rules
- Sorting complexities
- Python DSA complexities
- Input‑based complexities (O(a+b), O(a*b))
- Mnemonics, diagrams, examples

---

# 1️⃣ Time & Space Complexity

## **Time Complexity**
Measures how the execution time of an algorithm grows with input size.

## **Space Complexity**
Measures how much extra memory an algorithm needs.

---

# 2️⃣ Best, Average, Worst Case

| Case | Symbol | Meaning |
|------|--------|---------|
| **Best Case** | Ω (Omega) | Minimum possible time |
| **Average Case** | Θ (Theta) | Expected time |
| **Worst Case** | O (Big‑O) | Maximum possible time |

### **Simple Example (Linear Search)**
- **Ω(1):** element found at index 0
- **Θ(n/2):** found somewhere in middle
- **O(n):** not found / last index

---

# 3️⃣ Mathematical Meaning of Big‑O Symbols

### **Big‑O (O)** → Upper bound (worst case)
### **Big‑Theta (Θ)** → Tight bound (exact growth)
### **Big‑Omega (Ω)** → Lower bound (best case)

Example:
```
Ω(n) ≤ T(n) ≤ O(n²)
```

---

# 4️⃣ Big‑O Rules (Very Important)

### ✔ 1. Drop Constants
```
O(2n) → O(n)
O(n/5) → O(n)
```

### ✔ 2. Keep Only the Dominant Term
```
O(n² + n) → O(n²)
O(n³ + n) → O(n³)
```

### ✔ 3. Worst‑Case is default unless asked otherwise

### ✔ 4. Multiple independent inputs
```
O(a + b)  # separate loops
O(a * b)  # nested loops
```

---

# 5️⃣ Common Big‑O Complexities

## ⭐ O(1) — Constant Time
Does not depend on input size.
- Access `arr[i]`
- Dict lookup
- Swap two variables

```
value = arr[5]   # O(1)
```

---

## ⭐ O(log n) — Logarithmic
Divide and conquer.
- Binary Search
- Balanced BST operations
- Heap push/pop

```
Binary search reduces n → n/2 → n/4 → ...
```

---

## ⭐ O(n) — Linear
Proportional to input.
```
for item in arr:  # O(n)
```

---

## ⭐ O(n log n) — Linearithmic
Most efficient general sorting algorithms.
- Merge Sort
- Heap Sort
- QuickSort (avg)

---

## ⭐ O(n²) — Quadratic
Nested loops.
```
for i in n:
  for j in n:
    ...
```

---

# 6️⃣ Sorting Algorithms Time Complexity

| Algorithm | Best | Avg | Worst |
|----------|------|------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

---

# 7️⃣ Complexity with Different Inputs

## **O(a + b)** — independent loops
```
for i in a:
    ...
for j in b:
    ...
```

## **O(a * b)** — nested loops
```
for i in a:
    for j in b:
        ...
```

---

# 8️⃣ Python Data Structures Big‑O

## 📌 **List (Dynamic Array)**

| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Append | O(1) amortized |
| Insert at end | O(1) |
| Insert at start | O(n) |
| Delete from middle | O(n) |
| Search | O(n) |
| Sorting | O(n log n) |

---

## 📌 **Dictionary (Hash Map)**

| Operation | Avg | Worst |
|-----------|------|--------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case due to hash collisions.

---

## 📌 **Set**
Same as dict:
- Insert → O(1)
- Search → O(1)
- Remove → O(1)

---

# 9️⃣ Visual Diagrams (Text Format + Graph Shapes)

## 📊 Big-O Growth Graphs (ASCII Style)

### **1. O(1) — Constant**
```
|
|        ____
|       |    |
|_______|____|________________ n
```

### **2. O(log n) — Logarithmic**
```
|
|      ___
|     /
|    /
|___/_________________________ n
```

### **3. O(n) — Linear**
```
|
|        /
|       /
|      /
|_____/_______________________ n
```

### **4. O(n log n)**
```
|
|        /
|       /\
|      /  \
|_____/____\__________________ n
```

### **5. O(n²) — Quadratic**
```
|
|          /
|         /
|       _/
|    __/
|___/_________________________ n
```

### **6. O(2ⁿ) — Exponential**
```
|
|           /
|         _/
|      __/
|   __/
|__/__________________________ n
```

### **7. O(n!) — Factorial**
```
|
|            |
|            /\
|           /  \
|      ____/    \____
|_____/______________________ n
```

---

## 📈 Growth Graph Ordering

### 📈 Growth Graph Ordering
```
Fastest → Slowest (Graph above included):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### 🔁 Nested vs Sequential
```
Sequential loops → O(a + b)
Nested loops → O(a * b)
```

### 📦 Memory Example
```
def func(arr):
    x = 10       # O(1) space
    y = []       # O(1)
```
Total → O(1) extra memory.

---

# 🔟 Mnemonics to Memorize

### **O(1)** → "Same speed always"
### **O(log n)** → "Divide by 2 each step"
### **O(n)** → "Scan everything"
### **O(n²)** → "Loop inside loop"
### **O(n log n)** → "Smart sorting"

---

# 1️⃣1️⃣ Real Python Examples

### **Example: O(n)**
```
for x in arr:
    print(x)
```

### **Example: O(n²)**
```
for i in arr:
    for j in arr:
        print(i, j)
```

### **Example: O(log n)** — Binary Search
```
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
```

---

# 1️⃣2️⃣ Final Summary Table

| Complexity | Meaning |
|------------|---------|
| **O(1)** | Constant |
| **O(log n)** | Divide and conquer |
| **O(n)** | Linear |
| **O(n log n)** | Sorting level |
| **O(n²)** | Nested loops |
| **O(2ⁿ)** | Exponential recursion |
| **O(n!)** | Permutations |

---

If you want:
✅ A separate **DSA practice sheet**
✅ A **PDF export**
✅ A **flashcard version**
Just tell me!

