# Binary Search – Library Book Search

## Problem Statement

A university library has **10,00,000 books** arranged in sorted order, with book numbers from **1 to 10,00,000**.

A student wants to search for a particular book. The program must determine:

1. Whether the requested book exists.
2. The **index** of the book in the array.
3. The **location** of the book.

Since the books are sorted, **Binary Search** is used to efficiently find the required book.

---

## Objective

To implement the **Binary Search algorithm in Python** to search for a book in a sorted collection of 10,00,000 books.

---

## Algorithm

1. Start with the sorted array of books.
2. Set:

   * `low = 0`
   * `high = n - 1`
3. Find the middle index:

   ```text
   mid = low + (high - low) // 2
   ```
4. Compare the book at `mid` with the target book.
5. If `books[mid] == target`:

   * The book is found.
   * Return `mid`.
6. If `books[mid] < target`:

   * The target is in the right half.
   * Set `low = mid + 1`.
7. If `books[mid] > target`:

   * The target is in the left half.
   * Set `high = mid - 1`.
8. Repeat steps 3–7 while `low <= high`.
9. If `low > high`, the book does not exist.
10. If the book is found:

    * Array index = returned index.
    * Library location = index + 1.

---

## Python Program

```python
def binary_search(books, target):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if books[mid] == target:
            return mid

        elif books[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# 10 lakh books arranged from 1 to 10 lakh
books = list(range(1, 1000001))

# Student wants book number 75000
target = 75000

index = binary_search(books, target)

if index != -1:
    print("Book exists")
    print("Book number:", target)
    print("Index:", index)
    print("Location:", index + 1)
else:
    print("Book does not exist")
```

---

## Sample Input

```text
Number of books: 10,00,000
Book numbers: 1 to 10,00,000
Book to search: 75,000
```

## Sample Output

```text
Book exists
Book number: 75000
Index: 74999
Location: 75000
```

---

## Explanation

The books are stored in sorted order:

```text
Book Number:  1   2   3   4   ...   74999   75000   75001   ...
Array Index:  0   1   2   3   ...   74998   74999   75000   ...
```

Therefore, book **75,000** is stored at array index **74,999**.

Binary Search starts by checking the middle element of the current search range. Based on the comparison with the target, it eliminates half of the remaining books.

For example:

```text
Target = 75000

Middle → 500000
75000 < 500000
Search left half
```

The process continues until book `75000` is found.

Because the array uses **0-based indexing**, the index is:

```text
75000 - 1 = 74999
```

The library location, using 1-based numbering, is:

```text
74999 + 1 = 75000
```

---

## Complexity Analysis

### Time Complexity

```text
O(log n)
```

Binary Search divides the search space into half during every iteration.

For 10,00,000 books, only around **20 comparisons** are needed in the worst case.

### Space Complexity

```text
O(n)
```

The program stores the 10,00,000 book numbers in the `books` list.

The Binary Search algorithm itself uses:

```text
O(1)
```

additional space.

---

## Key Concepts Used

* Arrays / Lists
* Sorted Data
* Binary Search
* Iteration using `while` loop
* Conditional statements
* 0-based indexing
* Time and Space Complexity

---

## Conclusion

The program efficiently searches for a book among **10,00,000 sorted books** using Binary Search. Instead of checking every book sequentially, Binary Search repeatedly eliminates half of the search space, making the search significantly faster with **O(log n)** time complexity.
