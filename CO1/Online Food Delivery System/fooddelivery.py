# Online Food Delivery System

# Restaurant data
restaurants = {
    "1": {
        "name": "Pizza Palace",
        "menu": {
            "1": ("Margherita Pizza", 250),
            "2": ("Farmhouse Pizza", 350),
            "3": ("Garlic Bread", 150)
        }
    },
    "2": {
        "name": "Burger House",
        "menu": {
            "1": ("Veg Burger", 150),
            "2": ("Cheese Burger", 200),
            "3": ("French Fries", 100)
        }
    }
}


def login():
    print("\n--- User Login ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Simple validation
    if username == "admin" and password == "1234":
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False


def select_restaurant():
    print("\n--- Restaurants ---")

    for key, restaurant in restaurants.items():
        print(f"{key}. {restaurant['name']}")

    choice = input("Select a restaurant: ")

    if choice in restaurants:
        return restaurants[choice]

    print("Invalid restaurant selection.")
    return None


def display_menu(restaurant):
    print(f"\n--- {restaurant['name']} Menu ---")

    for key, item in restaurant["menu"].items():
        print(f"{key}. {item[0]} - ₹{item[1]}")


def order_food(restaurant):
    cart = []

    while True:
        display_menu(restaurant)

        choice = input("\nEnter food item number (0 to finish): ")

        if choice == "0":
            break

        if choice not in restaurant["menu"]:
            print("Invalid food item.")
            continue

        quantity = int(input("Enter quantity: "))

        item_name, price = restaurant["menu"][choice]

        cart.append({
            "name": item_name,
            "price": price,
            "quantity": quantity
        })

        print(f"{quantity} x {item_name} added to cart.")

    return cart


def calculate_bill(cart):
    subtotal = 0

    print("\n--- Order Summary ---")

    for item in cart:
        total = item["price"] * item["quantity"]
        subtotal += total
        print(
            f"{item['name']} x {item['quantity']} = ₹{total}"
        )

    gst = subtotal * 0.05
    delivery_charge = 40
    total_bill = subtotal + gst + delivery_charge

    print(f"\nSubtotal        : ₹{subtotal:.2f}")
    print(f"GST (5%)        : ₹{gst:.2f}")
    print(f"Delivery Charge : ₹{delivery_charge:.2f}")
    print(f"Total Bill      : ₹{total_bill:.2f}")

    return total_bill


def make_payment(amount):
    print("\n--- Payment ---")
    print(f"Amount to pay: ₹{amount:.2f}")

    print("1. UPI")
    print("2. Credit/Debit Card")
    print("3. Cash on Delivery")

    choice = input("Select payment method: ")

    if choice == "1":
        print("UPI payment successful!")

    elif choice == "2":
        print("Card payment successful!")

    elif choice == "3":
        print("Cash on Delivery selected.")

    else:
        print("Invalid payment method.")
        return False

    return True


def track_delivery():
    print("\n--- Delivery Tracking ---")

    statuses = [
        "Order Confirmed",
        "Food is being prepared",
        "Food picked up by delivery partner",
        "Out for delivery",
        "Order Delivered"
    ]

    for status in statuses:
        print(status)


def main():
    print("================================")
    print("     ONLINE FOOD DELIVERY")
    print("================================")

    # Step 1: Login
    if not login():
        return

    # Step 2: Restaurant selection
    restaurant = select_restaurant()

    if restaurant is None:
        return

    # Step 3: Food ordering
    cart = order_food(restaurant)

    if not cart:
        print("No items ordered.")
        return

    # Step 4: Calculate bill
    total_bill = calculate_bill(cart)

    # Step 5: Payment
    if not make_payment(total_bill):
        print("Payment failed. Order cancelled.")
        return

    # Step 6: Delivery tracking
    print("\nOrder placed successfully!")
    track_delivery()

    print("\nThank you for ordering!")


if __name__ == "__main__":
    main()