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