
# Online Shopping Cart System

## Overview

The Online Shopping Cart System is a Python-based, menu-driven application that allows users to manage products in a shopping cart and generate a final bill.

The program allows the user to add products, remove products, change product quantities, display the cart, apply a discount, calculate GST, and generate the final bill.

The program uses a Python dictionary to store product information such as price and quantity.

---

## Features

- Add products to the shopping cart
- Automatically increase quantity if a product already exists
- Remove products from the cart
- Change product quantity
- Remove a product by setting its quantity to zero or less
- Display all products in the cart
- Calculate the subtotal
- Apply a user-defined discount
- Calculate 18% GST
- Generate the final bill
- Interactive menu-driven interface

---

## Data Structure Used

The program uses a Python dictionary called `cart`.

```python
cart = {}
````

Each product is stored using the product name as the key.

Example:

```python
cart = {
    "Laptop": {
        "price": 50000,
        "quantity": 2
    },
    "Mouse": {
        "price": 1000,
        "quantity": 1
    }
}
```

The dictionary stores:

* Product name
* Product price
* Product quantity

---

# How the Program Works

## 1. Add Product

The user selects:

```text
1. Add Product
```

The program asks for:

* Product name
* Product price
* Quantity

Example:

```text
Enter product name: Laptop
Enter product price: 50000
Enter quantity: 2
```

If the product already exists in the cart, its quantity is increased.

For example, if the cart already contains:

```text
Laptop → Quantity: 2
```

and the user adds another 3 laptops:

```text
Laptop → Quantity: 5
```

If the product does not exist, a new entry is created.

---

## 2. Remove Product

The user selects:

```text
2. Remove Product
```

The program asks for the product name.

If the product exists, it is completely removed from the cart.

Example:

```text
Enter product name to remove: Mouse
Product removed successfully!
```

If the product does not exist:

```text
Product not found in cart.
```

---

## 3. Change Quantity

The user selects:

```text
3. Change Quantity
```

The program asks for the product name and the new quantity.

Example:

```text
Enter product name: Laptop
Enter new quantity: 3
Quantity updated successfully!
```

If the user enters a quantity of `0` or a negative value, the product is removed.

```text
Enter new quantity: 0
Product removed from cart.
```

---

## 4. Display Cart

The user selects:

```text
4. Display Cart
```

The program displays every product along with:

* Price
* Quantity
* Total amount for that product

The amount is calculated as:

```text
Amount = Price × Quantity
```

Example:

```text
========== SHOPPING CART ==========

Laptop | Price: ₹50000.00 | Quantity: 2 | Amount: ₹100000.00
Mouse | Price: ₹1000.00 | Quantity: 1 | Amount: ₹1000.00
```

If there are no products:

```text
Cart is empty.
```

---

# 5. Calculate Subtotal

The `calculate_subtotal()` function calculates the total cost of all products before applying any discount or GST.

The formula is:

```text
Subtotal = Σ (Product Price × Quantity)
```

For example:

```text
Laptop = ₹50,000 × 2 = ₹1,00,000
Mouse  = ₹1,000 × 1  = ₹1,000

Subtotal = ₹1,01,000
```

---

# 6. Generate Bill

The user selects:

```text
5. Generate Bill
```

The program first checks whether the cart is empty.

If the cart contains products, it calculates:

1. Subtotal
2. Discount
3. Amount after discount
4. GST
5. Final bill

---

## Discount Calculation

The program asks the user to enter the discount percentage.

```text
Enter discount percentage: 10
```

The discount is calculated using:

```text
Discount = Subtotal × Discount Percentage / 100
```

The amount after discount is:

```text
Amount After Discount = Subtotal - Discount
```

---

## GST Calculation

The program applies a fixed GST rate of **18%**.

```python
gst_percent = 18
```

GST is calculated on the amount after discount:

```text
GST = Amount After Discount × 18 / 100
```

---

## Final Bill Calculation

The final bill is calculated as:

```text
Total Bill = Amount After Discount + GST
```

---

# Bill Calculation Example

Suppose the cart contains:

```text
Laptop = ₹50,000 × 2
Mouse  = ₹1,000 × 1
```

### Step 1: Subtotal

```text
Subtotal = ₹1,00,000 + ₹1,000
         = ₹1,01,000
```

### Step 2: Discount

Suppose the discount is 10%:

```text
Discount = ₹1,01,000 × 10 / 100
         = ₹10,100
```

### Step 3: Amount After Discount

```text
₹1,01,000 - ₹10,100
= ₹90,900
```

### Step 4: GST

GST is 18%:

```text
GST = ₹90,900 × 18 / 100
    = ₹16,362
```

### Step 5: Final Bill

```text
Total Bill = ₹90,900 + ₹16,362
           = ₹1,07,262
```

---

# Menu Options

The program provides six options:

```text
===== ONLINE SHOPPING CART =====
1. Add Product
2. Remove Product
3. Change Quantity
4. Display Cart
5. Generate Bill
6. Exit
```

| Option | Operation               |
| ------ | ----------------------- |
| 1      | Add a product           |
| 2      | Remove a product        |
| 3      | Change product quantity |
| 4      | Display shopping cart   |
| 5      | Generate final bill     |
| 6      | Exit the program        |

---

# Technologies Used

* Python

# Python Concepts Used

### Dictionary

A dictionary is used to store product information.

```python
cart = {}
```

### Functions

The program is divided into separate functions:

```text
add_product()
remove_product()
change_quantity()
display_cart()
calculate_subtotal()
generate_bill()
```

This makes the program modular and easier to understand.

### Loops

A `while` loop continuously displays the menu until the user selects Exit.

`for` loops are used to process products in the cart.

### Conditional Statements

`if`, `elif`, and `else` statements are used for:

* Menu selection
* Product existence checking
* Quantity validation
* Empty cart checking

### Arithmetic Operations

The program performs calculations for:

* Product amount
* Subtotal
* Discount
* GST
* Final bill

### Formatted Strings

F-strings are used to display prices and amounts with two decimal places.

Example:

```python
f"₹{price:.2f}"
```

---

# Algorithm

1. Initialize an empty shopping cart.
2. Display the shopping cart menu.
3. Ask the user to select an option.
4. If the user selects **Add Product**:

   * Read product name, price, and quantity.
   * Check whether the product already exists.
   * If it exists, increase its quantity.
   * Otherwise, add a new product.
5. If the user selects **Remove Product**:

   * Search for the product.
   * Remove it if it exists.
6. If the user selects **Change Quantity**:

   * Search for the product.
   * Read the new quantity.
   * Remove the product if the quantity is zero or negative.
   * Otherwise, update the quantity.
7. If the user selects **Display Cart**:

   * Display all products, prices, quantities, and amounts.
8. If the user selects **Generate Bill**:

   * Calculate subtotal.
   * Read the discount percentage.
   * Calculate the discount.
   * Calculate the amount after discount.
   * Calculate 18% GST.
   * Calculate the final bill.
   * Display the complete bill.
9. If the user selects **Exit**, terminate the program.
10. For an invalid option, display an error message.
11. Continue until the user exits.

---

# Sample Execution

## Adding Products

```text
===== ONLINE SHOPPING CART =====
1. Add Product
2. Remove Product
3. Change Quantity
4. Display Cart
5. Generate Bill
6. Exit

Enter your choice: 1

Enter product name: Laptop
Enter product price: 50000
Enter quantity: 2

Product added successfully!
```

Adding another product:

```text
Enter your choice: 1

Enter product name: Mouse
Enter product price: 1000
Enter quantity: 1

Product added successfully!
```

---

## Displaying the Cart

```text
Enter your choice: 4

========== SHOPPING CART ==========

Laptop | Price: ₹50000.00 | Quantity: 2 | Amount: ₹100000.00
Mouse | Price: ₹1000.00 | Quantity: 1 | Amount: ₹1000.00
```

---

## Generating the Bill

```text
Enter your choice: 5

Enter discount percentage: 10

========== FINAL BILL ==========

========== SHOPPING CART ==========

Laptop | Price: ₹50000.00 | Quantity: 2 | Amount: ₹100000.00
Mouse | Price: ₹1000.00 | Quantity: 1 | Amount: ₹1000.00

--------------------------------
Subtotal          : ₹101000.00
Discount (10.0%) : ₹10100.00
Amount after discount : ₹90900.00
GST (18%)       : ₹16362.00
--------------------------------
TOTAL BILL        : ₹107262.00
================================
```

---

## Removing a Product

```text
Enter your choice: 2

Enter product name to remove: Mouse
Product removed successfully!
```

---

## Changing Quantity

```text
Enter your choice: 3

Enter product name: Laptop
Enter new quantity: 3

Quantity updated successfully!
```

---

## Exiting

```text
Enter your choice: 6

Thank you for shopping!
```

---

# Error Handling

### Empty Cart

If the user tries to generate a bill without products:

```text
Cart is empty.
```

### Product Not Found

When trying to remove a product that does not exist:

```text
Product not found in cart.
```

### Invalid Quantity

If the quantity is zero or negative:

```text
Product removed from cart.
```

### Invalid Menu Choice

If the user enters an option other than 1–6:

```text
Invalid choice. Please try again.
```

---

# Project Purpose

The purpose of this project is to demonstrate how Python programming concepts can be applied to develop a basic real-world online shopping and billing system.

The project demonstrates the use of dictionaries, functions, loops, conditional statements, user input, and arithmetic operations to manage products and calculate a final bill.

````

