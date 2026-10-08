import copy
print("   STUDENT RECORD MANAGEMENT SYSTEM")

while True:
    try:
        n = int(input("Enter the number of students: "))

        if n <= 0:
            raise ValueError

        break

    except ValueError:
        print("Please enter a valid positive integer.")

names = []
roll_numbers = []
marks = []

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")
    while True:
        try:
            name = input("Enter name: ").strip()

            if name == "":
                raise ValueError

            names.append(name)
            break

        except ValueError:
            print("Name cannot be empty.")
    while True:
        try:
            roll = int(input("Enter roll number: "))
            roll_numbers.append(roll)
            break

        except ValueError:
            print("Please enter a valid integer roll number.")

    student_marks = []
    for j in range(3):
        while True:
            try:
                mark = int(input(f"Enter marks for Subject {j + 1}: "))

                if mark < 0 or mark > 100:
                    raise ValueError

                student_marks.append(mark)
                break

            except ValueError:
                print("Please enter marks between 0 and 100.")

    marks.append(student_marks)



student_dict = dict(zip(roll_numbers, names))

print("\nStudent Dictionary")
print(student_dict)

# Convert names to uppercase
uppercase_names = [name.upper() for name in names]

print("\nNames in uppercase:")
print(uppercase_names)


# Names longer than 5 characters
long_names = [name for name in names if len(name) > 5]

print("\nNames longer than 5 characters:")
print(long_names)

# Count names starting with A
count_a = sum(
    1 for name in names
    if name.upper().startswith("A")
)

print("\nNumber of names starting with A:")
print(count_a)


# List comprehension
high_average_students = [
    names[i]
    for i in range(n)
    if sum(marks[i]) / len(marks[i]) > 75
]

print("\nStudents with average marks greater than 75:")
print(high_average_students)


# Even roll numbers
even_roll_numbers = [
    roll for roll in roll_numbers
    if roll % 2 == 0
]

print("\nEven roll numbers:")
print(even_roll_numbers)


# Tuple
first_student_tuple = tuple(marks[0])

print("\nFirst student's marks as tuple:")
print(first_student_tuple)


# Set of unique marks
unique_marks = set(
    mark
    for student in marks
    for mark in student
)

print("\nUnique marks:")
print(unique_marks)


# Shallow copy and deep copy
shallow_copy = copy.copy(marks)
deep_copy = copy.deepcopy(marks)


# Modify original marks
marks[0][0] = 100

print("\nCopy Demonstration")

print("\nOriginal marks:")
print(marks)

print("\nShallow copy:")
print(shallow_copy)

print("\nDeep copy:")
print(deep_copy)


print("\nProgram completed successfully!")
