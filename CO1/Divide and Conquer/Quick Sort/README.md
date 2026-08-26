# Quick Sort – E-Commerce Product Price Sorting

## Problem Statement

An e-commerce website contains a list of products with their prices. Customers often want to sort products based on price, such as **Low to High** or **High to Low**.

This project implements the **Quick Sort algorithm** to arrange products according to their prices in **ascending order**, from the lowest-priced product to the highest-priced product.

### Given Products

| Product     |   Price |
| ----------- | ------: |
| Laptop      | ₹65,000 |
| Smartphone  | ₹25,000 |
| Headphones  |  ₹3,000 |
| Smart Watch |  ₹8,000 |
| Tablet      | ₹30,000 |

---

## Objective

The objective of this project is to:

* Store product names and prices.
* Implement Quick Sort from scratch.
* Sort products based on their prices.
* Display products from lowest price to highest price.
* Demonstrate a real-world application of the Quick Sort algorithm.

---

## Algorithm

1. Store the product names and prices as pairs.
2. Check whether the list contains zero or one product.
3. If the list contains zero or one element, return the list.
4. Select the last product as the **pivot**.
5. Compare each remaining product's price with the pivot price.
6. Place products with prices less than or equal to the pivot into the **left list**.
7. Place products with prices greater than the pivot into the **right list**.
8. Recursively apply Quick Sort to the left and right lists.
9. Combine the sorted left list, pivot, and sorted right list.
10. Display the final sorted product list.

---

## Python Implementation

```python
def quick_sort(products):
    # Base case
    if len(products) <= 1:
        return products

    # Select the last product as pivot
    pivot = products[-1]

    left = []
    right = []

    # Partition the products
    for product in products[:-1]:

        if product[1] <= pivot[1]:
            left.append(product)
        else:
            right.append(product)

    # Recursively sort and combine
    return quick_sort(left) + [pivot] + quick_sort(right)


# Product data
products = [
    ("Laptop", 65000),
    ("Smartphone", 25000),
    ("Headphones", 3000),
    ("Smart Watch", 8000),
    ("Tablet", 30000)
]

# Sort products by price
sorted_products = quick_sort(products)

print("Products sorted by price (Low to High):")

for name, price in sorted_products:
    print(name, "- ₹", price)
```

---

## Sample Input

```text
Laptop - ₹65000
Smartphone - ₹25000
Headphones - ₹3000
Smart Watch - ₹8000
Tablet - ₹30000
```

---

## Sample Output

```text
Products sorted by price (Low to High):
Headphones - ₹ 3000
Smart Watch - ₹ 8000
Smartphone - ₹ 25000
Tablet - ₹ 30000
Laptop - ₹ 65000
```

---

## Working of Quick Sort

The original product list is:

```text
Laptop       - ₹65000
Smartphone   - ₹25000
Headphones   - ₹3000
Smart Watch  - ₹8000
Tablet       - ₹30000
```

The program selects the last product as the pivot:

```text
Pivot = Tablet - ₹30000
```

### Partition

Products with prices less than or equal to ₹30,000:

```text
Smartphone  - ₹25000
Headphones  - ₹3000
Smart Watch - ₹8000
```

Products with prices greater than ₹30,000:

```text
Laptop - ₹65000
```

Quick Sort is then recursively applied to these groups.

After all partitions and recursive sorting, the final result is:

```text
Headphones  - ₹3000
Smart Watch  - ₹8000
Smartphone   - ₹25000
Tablet       - ₹30000
Laptop       - ₹65000
```

---

## Why Quick Sort?

Quick Sort is a **Divide and Conquer** algorithm.

It works by selecting a **pivot** and dividing the remaining elements into two groups:

```text
                  Pivot
                    ↓
              ₹30,000
             /         \
      Smaller          Larger
        prices          prices
          ↓                ↓
     Sort recursively  Sort recursively
             \          /
                Combine
```

This makes Quick Sort useful for applications where a large collection of data needs to be sorted efficiently.

---

## Real-World Application

This algorithm can be used in an e-commerce website when a customer selects:

```text
Sort By → Price: Low to High
```

For example:

```text
₹3,000   → Headphones
₹8,000   → Smart Watch
₹25,000  → Smartphone
₹30,000  → Tablet
₹65,000  → Laptop
```

The website can use a sorting algorithm to arrange the products before displaying them to the customer.

---

## Complexity Analysis

### Best Case

```text
O(n log n)
```

The pivot divides the list into reasonably balanced parts.

### Average Case

```text
O(n log n)
```

On average, Quick Sort performs efficiently.

### Worst Case

```text
O(n²)
```

The worst case occurs when the pivot repeatedly creates highly unbalanced partitions.

### Space Complexity

For this implementation:

```text
O(n)
```

Additional lists are created during the partitioning process.

---

## Key Concepts Used

* Quick Sort
* Divide and Conquer
* Pivot
* Partitioning
* Recursion
* Python Lists
* Tuples
* Sorting
* Time Complexity
* Space Complexity

---

## Conclusion

This project demonstrates a real-world application of **Quick Sort** in an e-commerce product sorting system.

The program successfully sorts products according to their prices in ascending order. Quick Sort uses the **Divide and Conquer** approach and has an average time complexity of **O(n log n)**, making it an efficient sorting algorithm for many practical applications.
