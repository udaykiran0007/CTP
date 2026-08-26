# Student Attendance Analysis System

students = []

n = int(input("Enter number of students: "))

# Input student details
for i in range(n):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")
    total_classes = int(input("Enter total classes conducted: "))
    attended = int(input("Enter classes attended: "))

    attendance = (attended / total_classes) * 100

    students.append({
        "name": name,
        "total": total_classes,
        "attended": attended,
        "attendance": attendance
    })


# Display attendance of all students
print("\n===== ATTENDANCE DETAILS =====")

for student in students:
    print(
        f"{student['name']} : "
        f"{student['attendance']:.2f}%"
    )


# Students below 75%
print("\n===== STUDENTS BELOW 75% =====")

below_75 = []

for student in students:
    if student["attendance"] < 75:
        below_75.append(student)

if len(below_75) == 0:
    print("No student is below 75% attendance.")
else:
    for student in below_75:
        print(
            f"{student['name']} : "
            f"{student['attendance']:.2f}%"
        )


# Find student with highest attendance
highest = students[0]

for student in students:
    if student["attendance"] > highest["attendance"]:
        highest = student

print("\n===== HIGHEST ATTENDANCE =====")
print(
    f"{highest['name']} : "
    f"{highest['attendance']:.2f}%"
)


# Calculate overall attendance
total_classes = 0
total_attended = 0

for student in students:
    total_classes += student["total"]
    total_attended += student["attended"]

overall_attendance = (total_attended / total_classes) * 100

print("\n===== OVERALL ATTENDANCE =====")
print(f"Total Classes Conducted : {total_classes}")
print(f"Total Classes Attended  : {total_attended}")
print(f"Overall Attendance      : {overall_attendance:.2f}%")