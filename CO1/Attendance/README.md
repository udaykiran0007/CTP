
# Student Attendance Analysis System

## Overview

The Student Attendance Analysis System is a Python-based program that analyzes the attendance of multiple students.

The program accepts the number of students and collects each student's name, total number of classes conducted, and number of classes attended. It then calculates and displays individual attendance percentages, identifies students below 75% attendance, finds the student with the highest attendance, and calculates the overall attendance of all students.

## Features

- Accept the number of students
- Accept student name
- Accept total classes conducted
- Accept classes attended
- Calculate individual attendance percentage
- Display attendance details of all students
- Identify students below 75% attendance
- Find the student with the highest attendance
- Calculate overall classes conducted
- Calculate overall classes attended
- Calculate overall attendance percentage

## Attendance Calculation

The attendance percentage of each student is calculated using:

```text
Attendance Percentage =
(Classes Attended / Total Classes Conducted) × 100
````

The overall attendance is calculated using the total classes conducted and total classes attended by all students:

```text
Overall Attendance =
(Total Classes Attended / Total Classes Conducted) × 100
```

## Program Working

### 1. Input Number of Students

The program first asks the user to enter the number of students to be analyzed.

```text
Enter number of students: 3
```

### 2. Collect Student Details

For each student, the program accepts:

* Student name
* Total classes conducted
* Classes attended

The attendance percentage is calculated immediately and the details are stored in a list of dictionaries.

### 3. Display Attendance Details

The program displays the attendance percentage of every student.

For example:

```text
Rahul : 90.00%
Priya : 70.00%
Arjun : 82.00%
```

### 4. Find Students Below 75%

The program checks the attendance percentage of every student.

Students whose attendance is less than 75% are displayed separately.

```text
===== STUDENTS BELOW 75% =====
Priya : 70.00%
```

### 5. Find Highest Attendance

The program compares the attendance percentage of all students and identifies the student with the highest attendance.

```text
===== HIGHEST ATTENDANCE =====
Rahul : 90.00%
```

### 6. Calculate Overall Attendance

The program adds the total classes conducted and total classes attended by all students.

It then calculates the overall attendance percentage.

## Technologies Used

* Python

## Python Concepts Used

* Variables
* Lists
* Dictionaries
* `for` loops
* `if` conditions
* User input
* Arithmetic operations
* Formatted strings (f-strings)
* List manipulation
* Comparison and searching

## Data Structure Used

The program uses a **list of dictionaries** to store student information.

Each student is represented as:

```python
{
    "name": name,
    "total": total_classes,
    "attended": attended,
    "attendance": attendance
}
```

The list allows the program to store and process information for multiple students.

## Sample Input

```text
Enter number of students: 3

Student 1
Enter student name: Rahul
Enter total classes conducted: 50
Enter classes attended: 45

Student 2
Enter student name: Priya
Enter total classes conducted: 50
Enter classes attended: 35

Student 3
Enter student name: Arjun
Enter total classes conducted: 50
Enter classes attended: 41
```

## Sample Output

```text
===== ATTENDANCE DETAILS =====
Rahul : 90.00%
Priya : 70.00%
Arjun : 82.00%

===== STUDENTS BELOW 75% =====
Priya : 70.00%

===== HIGHEST ATTENDANCE =====
Rahul : 90.00%

===== OVERALL ATTENDANCE =====
Total Classes Conducted : 150
Total Classes Attended  : 121
Overall Attendance      : 80.67%
```

## How to Run

Open a terminal in the `Attendance` folder and run:

```bash
python attendance.py
```

## Example

The program can be used by a teacher or administrator to quickly analyze attendance records for a group of students and identify students whose attendance is below the required 75% threshold.

## Purpose

The purpose of this project is to demonstrate how basic Python programming concepts and data structures can be used to solve a practical student attendance analysis problem.

````



