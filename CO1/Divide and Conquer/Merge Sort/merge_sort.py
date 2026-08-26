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

# Scholarship eligibility
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