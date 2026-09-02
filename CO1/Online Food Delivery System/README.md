# Online Food Delivery System

## 1. Introduction

The **Online Food Delivery System** is a Python-based application that simulates the basic process of ordering food online.

The system allows a user to:

* Login to the application
* Select a restaurant
* View the restaurant menu
* Select food items and quantities
* Add items to the order
* Calculate the bill
* Select a payment method
* Track the delivery status

This project demonstrates **problem decomposition**, where a large problem is divided into smaller and manageable subproblems.

---

## 2. Problem Decomposition

The complete food delivery system is divided into the following modules:

1. **User Login**
2. **Restaurant Selection**
3. **Food Selection**
4. **Order Management**
5. **Bill Calculation**
6. **Payment Processing**
7. **Delivery Tracking**

Each module performs a specific task.

---

## 3. Algorithm

### Step 1: Start

Start the food delivery application.

### Step 2: Login

* Ask the user for username and password.
* Validate the credentials.
* If the credentials are invalid, terminate the program.

### Step 3: Select Restaurant

* Display the list of restaurants.
* Ask the user to select a restaurant.
* Display the selected restaurant's menu.

### Step 4: Order Food

* Display available food items.
* Ask the user to select food items.
* Ask for the quantity.
* Add the selected items to the cart.
* Continue until the user chooses to finish ordering.

### Step 5: Calculate Bill

Calculate:

```text
Subtotal = Sum of (Food Price × Quantity)

GST = Subtotal × 5%

Total Bill = Subtotal + GST + Delivery Charge
```

### Step 6: Payment

* Display available payment methods.
* Allow the user to select UPI, Card, or Cash on Delivery.
* Process the selected payment method.

### Step 7: Track Delivery

Display the order status:

```text
Order Confirmed
       ↓
Food is being prepared
       ↓
Food picked up
       ↓
Out for delivery
       ↓
Order Delivered
```

### Step 8: End

Display the completion message and terminate the program.

---

## 4. Technologies Used

* **Programming Language:** Python
* **Data Structures:** Dictionary, List
* **Concepts:** Functions, Loops, Conditional Statements, Input/Output

---

## 5. How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python food_delivery.py
```

---

## 6. Login Credentials

For demonstration purposes:

```text
Username: admin
Password: 1234
```

---

## 7. Sample Execution

```text
================================
     ONLINE FOOD DELIVERY
================================

--- User Login ---
Enter username: admin
Enter password: 1234
Login successful!

--- Restaurants ---
1. Pizza Palace
2. Burger House

Select a restaurant: 1

--- Pizza Palace Menu ---
1. Margherita Pizza - ₹250
2. Farmhouse Pizza - ₹350
3. Garlic Bread - ₹150

Enter food item number (0 to finish): 1
Enter quantity: 2

2 x Margherita Pizza added to cart.

Enter food item number (0 to finish): 3
Enter quantity: 1

1 x Garlic Bread added to cart.

Enter food item number (0 to finish): 0

--- Order Summary ---
Margherita Pizza x 2 = ₹500
Garlic Bread x 1 = ₹150

Subtotal        : ₹650.00
GST (5%)        : ₹32.50
Delivery Charge : ₹40.00
Total Bill      : ₹722.50

--- Payment ---
Amount to pay: ₹722.50

1. UPI
2. Credit/Debit Card
3. Cash on Delivery

Select payment method: 1

UPI payment successful!

Order placed successfully!

--- Delivery Tracking ---
Order Confirmed
Food is being prepared
Food picked up by delivery partner
Out for delivery
Order Delivered

Thank you for ordering!
```

---
Time Complexity  : O(n)
Space Complexity : O(n)

## 8. Conclusion

The Online Food Delivery System demonstrates how a complex real-world application can be solved using **problem decomposition**.



