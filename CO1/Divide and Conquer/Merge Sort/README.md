# Merge Sort – Scholarship Eligibility

## Problem Statement

A university has a list of students along with their marks. The university wants to identify students who are eligible for a scholarship.

The given student details are:

| Student | Marks |
| ------- | ----: |
| Anita   |    95 |
| Vivek   |    83 |
| Lakshmi |    67 |
| Ramesh  |    97 |
| Kumar   |    85 |

A student is eligible for the scholarship if their marks are **85 or above**.

The program uses the **Merge Sort algorithm** to sort students according to their marks in descending order and then selects the eligible students.

---

## Objective

To implement the **Merge Sort algorithm in Python** to:

* Store student names and marks.
* Sort students based on marks in descending order.
* Identify students eligible for the scholarship.
* Display the sorted student list and eligible students.

---

## Algorithm

1. Store the student names and marks as pairs.
2. Set the scholarship cutoff mark to `85`.
3. Divide the student list into two halves.
4. Recursively divide each half until each part contains one student.
5. Compare the marks of students from the divided lists.
6. Merge the lists in descending order of marks.
7. After sorting, traverse the sorted list.
8. Select students whose marks are greater than or equal to `85`.
9. Display the eligible students.

---

## Python Program

```python
def merge_sort(students):
    # Base case
    if len(students) <= 1:
        return students

    # Find middle
    mid = len(students) // 2

    # Divide the list
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    # Merge the sorted lists
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Sort in descending order of marks
    while i < len(left) and j < len(right):

        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Student data
students = [
    ("Anita", 95),
    ("Vivek", 83),
    ("Lakshmi", 67),
    ("Ramesh", 97),
    ("Kumar", 85)
]

# Scholarship eligibility cutoff
cutoff = 85

# Sort students using Merge Sort
sorted_students = merge_sort(students)

print("Students sorted by marks:")

for name, marks in sorted_students:
    print(name, "-", marks)

print("\nScholarship Eligible Students:")

for name, marks in sorted_students:
    if marks >= cutoff:
        print(name, "-", marks)
```

---

## Sample Input

```text
Anita   95
Vivek   83
Lakshmi 67
Ramesh  97
Kumar   85

Scholarship cutoff = 85
```

---

## Sample Output

```text
Students sorted by marks:
Ramesh - 97
Anita - 95
Kumar - 85
Vivek - 83
Lakshmi - 67

Scholarship Eligible Students:
Ramesh - 97
Anita - 95
Kumar - 85
```

---

## Merge Sort Explanation

The original list is:

```text
Anita - 95
Vivek - 83
Lakshmi - 67
Ramesh - 97
Kumar - 85
```

### Step 1: Divide

The list is divided into two parts:

```text
Left:
Anita - 95
Vivek - 83
Lakshmi - 67

Right:
Ramesh - 97
Kumar - 85
```

The lists are further divided until each list contains one student.

### Step 2: Merge

The individual elements are compared based on marks.

Since we need **descending order**, the student with the higher mark is placed first.

The final sorted list is:

```text
Ramesh - 97
Anita - 95
Kumar - 85
Vivek - 83
Lakshmi - 67
```

### Step 3: Select Eligible Students

The scholarship cutoff is:

```text
85
```

Therefore:

```text
Ramesh - 97  → Eligible
Anita - 95   → Eligible
Kumar - 85   → Eligible
Vivek - 83   → Not Eligible
Lakshmi - 67 → Not Eligible
```

---

## Complexity Analysis

### Time Complexity

```text
O(n log n)
```

Merge Sort divides the list into halves and then merges the sorted halves.

### Space Complexity

```text
O(n)
```

Additional space is required to store the temporary lists during merging.

---

## Key Concepts Used

* Merge Sort
* Divide and Conquer
* Python Lists
* Tuples
* Recursion
* Sorting
* Conditional Statements
* Time Complexity
* Space Complexity

---

## Conclusion

The program successfully uses **Merge Sort** to arrange students according to their marks in descending order. After sorting, students with marks **85 or above** are selected as scholarship-eligible students.

For the given data, **Ramesh, Anita, and Kumar** are eligible for the scholarship.
