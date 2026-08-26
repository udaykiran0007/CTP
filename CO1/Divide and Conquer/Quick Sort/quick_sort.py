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