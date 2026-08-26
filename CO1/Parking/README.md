
# Smart Parking System

## Overview

The Smart Parking System is a Python-based parking management program developed using Object-Oriented Programming (OOP).

The system manages parking slots, allows vehicles to enter and leave the parking area, records vehicle entry time, calculates parking duration, and generates the parking charge based on the time spent in the parking area.

By default, the parking lot contains **100 parking slots**, and the parking charge is **₹20 per hour**.

---

## Features

- Park a vehicle in an available slot
- Automatically allocate the first available parking slot
- Check whether the parking area is full
- Remove a vehicle from the parking lot
- Record vehicle entry time
- Calculate parking duration
- Calculate parking charges
- Display total, occupied, and available slots
- Interactive menu-driven interface

---

## Default Configuration

The `ParkingLot` class is initialized with:

```python
ParkingLot(total_slots=100, rate_per_hour=20)
````

Therefore:

```text
Total Parking Slots : 100
Rate per Hour       : ₹20
```

The values can also be changed when creating the `ParkingLot` object.

---

## How the Program Works

### 1. Create the Parking Lot

The program creates a `ParkingLot` object:

```python
parking = ParkingLot()
```

The constructor initializes:

* Total number of parking slots
* Parking rate per hour
* Dictionary for occupied slots
* Dictionary for vehicle entry times

---

## 2. Store Parking Information

The program uses two dictionaries.

### Slots Dictionary

```python
self.slots = {}
```

This stores the relationship between the parking slot and vehicle number.

Example:

```text
Slot 1 → AP01AB1234
Slot 2 → AP02CD5678
```

### Entry Time Dictionary

```python
self.entry_time = {}
```

This stores the entry time for each vehicle.

Example:

```text
AP01AB1234 → 10:30 AM
AP02CD5678 → 11:15 AM
```

---

## 3. Park a Vehicle

When the user selects:

```text
1. Park Vehicle
```

the program asks for the vehicle number.

The system first checks whether the parking lot is full.

If space is available, it searches from slot 1 onwards and assigns the first available slot.

Example:

```text
Enter choice: 1
Enter Vehicle Number: AP01AB1234

Vehicle AP01AB1234 parked at Slot 1
```

The entry time is recorded using:

```python
datetime.now()
```

---

## 4. Check Parking Availability

When the user selects:

```text
3. Check Availability
```

the program displays:

* Total slots
* Occupied slots
* Available slots
* Current parking status

The number of available slots is calculated as:

```text
Available Slots = Total Slots - Occupied Slots
```

Example:

```text
------ Parking Status ------
Total Slots     : 100
Occupied Slots  : 1
Available Slots : 99
Status : Available
----------------------------
```

---

## 5. Remove a Vehicle

When the user selects:

```text
2. Remove Vehicle
```

the program asks for the vehicle number.

It searches the parking slots to find the vehicle.

If the vehicle is found, the program:

1. Records the exit time.
2. Calculates the parking duration.
3. Rounds the duration up to the next complete hour.
4. Calculates the parking charge.
5. Frees the parking slot.
6. Removes the vehicle's entry-time record.

---

## 6. Calculate Parking Duration

The program calculates the duration using:

```python
duration = exit_time - self.entry_time[vehicle_no]
```

The duration is converted into hours using:

```python
hours = math.ceil(duration.total_seconds() / 3600)
```

`math.ceil()` ensures that any partial hour is charged as a complete hour.

For example:

```text
Parking duration = 1 hour 20 minutes
Charged duration = 2 hours
```

---

## 7. Calculate Parking Charge

The parking charge is calculated using:

```text
Charge = Number of Hours × Rate per Hour
```

With the default rate:

```text
Rate = ₹20/hour
```

For example:

```text
Parking Time = 3 hours
Rate         = ₹20/hour

Total Charge = 3 × ₹20
             = ₹60
```

---

## 8. Exit the Program

When the user selects:

```text
4. Exit
```

the program displays:

```text
Thank You!
```

and terminates the program.

---

# Menu Options

The program provides four options:

```text
===== SMART PARKING SYSTEM =====
1. Park Vehicle
2. Remove Vehicle
3. Check Availability
4. Exit
```

| Option | Operation                           |
| ------ | ----------------------------------- |
| 1      | Park a vehicle                      |
| 2      | Remove a vehicle and calculate bill |
| 3      | Display parking status              |
| 4      | Exit the program                    |

---

# Technologies Used

* Python
* `datetime` module
* `math` module

---

# Concepts Used

### Object-Oriented Programming

The program uses a `ParkingLot` class to represent the parking system.

### Class

```python
class ParkingLot:
```

The class contains the data and operations required to manage the parking lot.

### Constructor

```python
def __init__(self, total_slots=100, rate_per_hour=20):
```

The constructor initializes the parking system.

### Methods

The class contains methods for different parking operations:

```text
available_slots()
is_full()
park_vehicle()
remove_vehicle()
status()
```

### Dictionaries

Two dictionaries are used to maintain parking information:

```python
self.slots = {}
self.entry_time = {}
```

### Date and Time

The `datetime` module is used to record vehicle entry and exit times.

### Mathematical Calculation

The `math.ceil()` function is used to round parking duration up to the next whole hour.

### Loops and Conditional Statements

The program uses:

* `while` loop for the interactive menu
* `for` loops to search parking slots
* `if-elif-else` statements for menu selection and validation

---

# Algorithm

1. Create a parking lot with 100 slots and a rate of ₹20 per hour.
2. Display the main menu.
3. Ask the user to select an operation.
4. If the user selects **Park Vehicle**:

   * Check whether the parking lot is full.
   * Find the first available slot.
   * Assign the slot to the vehicle.
   * Store the vehicle's entry time.
5. If the user selects **Remove Vehicle**:

   * Search for the vehicle.
   * Record the exit time.
   * Calculate parking duration.
   * Round the duration upward to a complete hour.
   * Calculate the parking charge.
   * Release the parking slot.
6. If the user selects **Check Availability**:

   * Display total, occupied, and available slots.
7. If the user selects **Exit**, terminate the program.
8. For an invalid choice, display an error message.
9. Continue until the user selects Exit.

---

# Sample Execution

## Parking a Vehicle

```text
===== SMART PARKING SYSTEM =====
1. Park Vehicle
2. Remove Vehicle
3. Check Availability
4. Exit

Enter choice: 1
Enter Vehicle Number: AP01AB1234
Vehicle AP01AB1234 parked at Slot 1
```

## Checking Availability

```text
===== SMART PARKING SYSTEM =====
1. Park Vehicle
2. Remove Vehicle
3. Check Availability
4. Exit

Enter choice: 3

------ Parking Status ------
Total Slots     : 100
Occupied Slots  : 1
Available Slots : 99
Status : Available
----------------------------
```

## Removing a Vehicle

If the vehicle has been parked for approximately 2 hours:

```text
===== SMART PARKING SYSTEM =====
1. Park Vehicle
2. Remove Vehicle
3. Check Availability
4. Exit

Enter choice: 2
Enter Vehicle Number: AP01AB1234

Vehicle AP01AB1234 left Slot 1
Parking Time : 2 hour(s)
Total Charge : ₹40
```

## Exiting

```text
===== SMART PARKING SYSTEM =====
1. Park Vehicle
2. Remove Vehicle
3. Check Availability
4. Exit

Enter choice: 4
Thank You!
```

---

# Error Handling

### Parking Full

If all parking slots are occupied:

```text
Parking Area is FULL!
```

### Vehicle Not Found

If a user attempts to remove a vehicle that is not parked:

```text
Vehicle not found!
```

### Invalid Menu Choice

If the user enters an option other than 1–4:

```text
Invalid Choice
```

---

# Project Purpose

The purpose of this project is to demonstrate how Python and Object-Oriented Programming can be used to design a real-world parking management system.

The project combines classes, objects, dictionaries, loops, conditional statements, date-time operations, and mathematical calculations into a single practical application.

````


