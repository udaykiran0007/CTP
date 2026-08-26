# Online Shopping Cart System

cart = {}

# Add product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {
            "price": price,
            "quantity": quantity
        }

    print("Product added successfully!")


# Remove product
def remove_product():
    name = input("Enter product name to remove: ")

    if name in cart:
        del cart[name]
        print("Product removed successfully!")
    else:
        print("Product not found in cart.")


# Change quantity
def change_quantity():
    name = input("Enter product name: ")

    if name in cart:
        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            del cart[name]
            print("Product removed from cart.")
        else:
            cart[name]["quantity"] = quantity
            print("Quantity updated successfully!")
    else:
        print("Product not found.")


# Display cart
def display_cart():
    print("\n========== SHOPPING CART ==========")

    if len(cart) == 0:
        print("Cart is empty.")
        return

    for name, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]
        amount = price * quantity

        print(
            f"{name} | "
            f"Price: ₹{price:.2f} | "
            f"Quantity: {quantity} | "
            f"Amount: ₹{amount:.2f}"
        )


# Calculate subtotal
def calculate_subtotal():
    subtotal = 0

    for details in cart.values():
        subtotal += details["price"] * details["quantity"]

    return subtotal


# Generate bill
def generate_bill():

    if len(cart) == 0:
        print("Cart is empty.")
        return

    subtotal = calculate_subtotal()

    # Discount
    discount_percent = float(
        input("Enter discount percentage: ")
    )

    discount = subtotal * discount_percent / 100

    amount_after_discount = subtotal - discount

    # GST
    gst_percent = 18

    gst = amount_after_discount * gst_percent / 100

    total_bill = amount_after_discount + gst

    print("\n========== FINAL BILL ==========")

    display_cart()

    print("--------------------------------")
    print(f"Subtotal          : ₹{subtotal:.2f}")
    print(f"Discount ({discount_percent}%) : ₹{discount:.2f}")
    print(f"Amount after discount : ₹{amount_after_discount:.2f}")
    print(f"GST ({gst_percent}%)       : ₹{gst:.2f}")
    print("--------------------------------")
    print(f"TOTAL BILL        : ₹{total_bill:.2f}")
    print("================================")


# Main program
while True:

    print("\n===== ONLINE SHOPPING CART =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Display Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        remove_product()

    elif choice == "3":
        change_quantity()

    elif choice == "4":
        display_cart()

    elif choice == "5":
        generate_bill()

    elif choice == "6":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")