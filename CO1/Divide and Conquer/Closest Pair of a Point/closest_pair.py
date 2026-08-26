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

    # Recursively find closest pair in both halves
    left_distance, left_pair = closest_pair(left)
    right_distance, right_pair = closest_pair(right)

    # Find minimum distance from both halves
    if left_distance < right_distance:
        min_distance = left_distance
        closest = left_pair
    else:
        min_distance = right_distance
        closest = right_pair

    # Find points near the dividing line
    mid_x = points[mid][0]

    strip = []

    for point in points:
        if abs(point[0] - mid_x) < min_distance:
            strip.append(point)

    # Check points in the strip
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

# Sort points according to x-coordinate
points.sort()

min_distance, closest = closest_pair(points)

print("Delivery Locations:")
for point in points:
    print(point)

print("\nClosest Pair:")
print(closest[0], "and", closest[1])

print("Minimum Distance:", round(min_distance, 2))