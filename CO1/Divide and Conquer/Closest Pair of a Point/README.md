# Closest Pair of Points – Delivery Location Analysis

## Problem Statement

A delivery company has multiple delivery locations represented as points on a two-dimensional coordinate plane.

The company wants to identify the **two delivery locations that are closest to each other**. Finding nearby locations can help in delivery planning, assigning delivery zones, and optimizing logistics.

Each location is represented using an `(x, y)` coordinate.

The program uses the **Closest Pair of Points algorithm** based on the **Divide and Conquer** technique to find the pair of points with the minimum Euclidean distance.

---

## Given Delivery Locations

```text
(2, 3)
(12, 30)
(40, 50)
(5, 1)
(12, 10)
(3, 4)
```

---

## Objective

The objective of this project is to:

* Represent delivery locations as 2D points.
* Calculate the distance between two points.
* Find the closest pair of points.
* Implement the Closest Pair algorithm using Divide and Conquer.
* Display the closest locations and their minimum distance.

---

## Distance Formula

The Euclidean distance between two points:

```text
P1 = (x1, y1)
P2 = (x2, y2)
```

is calculated using:

```text
distance = √((x2 - x1)² + (y2 - y1)²)
```

---

## Algorithm

1. Store all delivery locations as `(x, y)` coordinates.
2. Sort the points according to their x-coordinate.
3. Divide the points into two halves.
4. Recursively find the closest pair in the left half.
5. Recursively find the closest pair in the right half.
6. Find the smaller distance between the two halves.
7. Create a strip containing points close to the dividing line.
8. Compare points within the strip.
9. Update the minimum distance if a closer pair is found.
10. Return the closest pair and its distance.

---

## Python Implementation

```python
import math


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def brute_force(points):
    min_distance = float("inf")
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            d = distance(points[i], points[j])

            if d < min_distance:
                min_distance = d
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


def closest_pair(points):

    # Base case
    if len(points) <= 3:
        return brute_force(points)

    # Divide
    mid = len(points) // 2

    left = points[:mid]
    right = points[mid:]

    # Recursive calls
    left_distance, left_pair = closest_pair(left)
    right_distance, right_pair = closest_pair(right)

    # Select smaller distance
    if left_distance < right_distance:
        min_distance = left_distance
        closest = left_pair
    else:
        min_distance = right_distance
        closest = right_pair

    # Create strip around dividing line
    mid_x = points[mid][0]

    strip = []

    for point in points:
        if abs(point[0] - mid_x) < min_distance:
            strip.append(point)

    # Compare points in strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):

            d = distance(strip[i], strip[j])

            if d < min_distance:
                min_distance = d
                closest = (strip[i], strip[j])

    return min_distance, closest


# Delivery locations
points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4)
]

# Sort according to x-coordinate
points.sort()

# Find closest pair
min_distance, closest = closest_pair(points)

print("Delivery Locations:")

for point in points:
    print(point)

print("\nClosest Pair:")
print(closest[0], "and", closest[1])

print("Minimum Distance:", round(min_distance, 2))
```

---

## Sample Input

```text
(2, 3)
(12, 30)
(40, 50)
(5, 1)
(12, 10)
(3, 4)
```

---

## Sample Output

```text
Delivery Locations:
(2, 3)
(3, 4)
(5, 1)
(12, 10)
(12, 30)
(40, 50)

Closest Pair:
(2, 3) and (3, 4)

Minimum Distance: 1.41
```

---

## Working of the Algorithm

The points are first sorted according to their x-coordinate:

```text
(2, 3)
(3, 4)
(5, 1)
(12, 10)
(12, 30)
(40, 50)
```

The list is divided into two halves:

```text
Left Half:

(2, 3)
(3, 4)
(5, 1)


Right Half:

(12, 10)
(12, 30)
(40, 50)
```

The algorithm recursively finds the closest pair in each half.

For the left half:

```text
(2, 3) and (3, 4)
```

Distance:

```text
√((3 - 2)² + (4 - 3)²)

= √2

≈ 1.41
```

The algorithm then checks whether there is an even closer pair crossing the dividing line.

After checking the relevant points, the minimum distance remains:

```text
1.41
```

Therefore:

```text
Closest Pair = (2, 3), (3, 4)
Minimum Distance = 1.41
```

---

## Divide and Conquer Approach

The algorithm follows three main steps:

### 1. Divide

Split the points into two halves based on their x-coordinate.

```text
             All Points
                 |
        -------------------
        |                 |
    Left Half         Right Half
```

### 2. Conquer

Recursively find the closest pair in each half.

```text
Left → Closest Pair
Right → Closest Pair
```

### 3. Combine

Check the points near the dividing line to determine whether a pair crossing the two halves is closer.

```text
Left closest distance
          +
Right closest distance
          ↓
    Minimum distance
          ↓
 Check dividing strip
```

---

## Real-World Applications

The Closest Pair of Points algorithm can be used in:

* GPS and navigation systems
* Delivery route planning
* Finding nearby warehouses
* Emergency service location planning
* Telecommunication tower placement
* Geographic Information Systems (GIS)
* Airport and transportation planning
* Clustering and spatial data analysis

For this project, the algorithm is used to identify **nearby delivery locations**.

---

## Complexity Analysis

### Brute Force Approach

If every pair of points is compared, the time complexity is:

```text
O(n²)
```

because there can be approximately `n²` pairs.

### Divide and Conquer Approach

The standard Closest Pair of Points algorithm has:

```text
O(n log n)
```

time complexity when implemented efficiently.

The recursive division reduces the problem into smaller subproblems, while the strip is checked efficiently.

### Space Complexity

The implementation uses additional lists for the recursive divisions and strip:

```text
O(n)
```

---

## Key Concepts Used

* Closest Pair of Points
* Divide and Conquer
* Recursion
* Euclidean Distance
* 2D Coordinates
* Sorting
* Python Lists
* Mathematical Functions
* Time Complexity
* Space Complexity

---

## Conclusion

This project demonstrates how the **Closest Pair of Points algorithm** can solve a practical location-based problem.

For the given delivery locations, the closest two locations are:

```text
(2, 3) and (3, 4)
```

with a minimum distance of approximately:

```text
1.41 units
```

The Divide and Conquer approach improves the efficiency compared with checking every possible pair, making the technique useful for large spatial datasets.
