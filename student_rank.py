from abc import ABC, abstractmethod
class Evaluation(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

class Student(Person, Evaluation):
    student_count = 0
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
        Student.student_count += 1

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / 3

    # calculating the grade
    def calculate_grade(self):
        avg = self.average_marks()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"
        
    def __lt__(self, other):
        return self.total_marks() < other.total_marks()

    # static method
    @staticmethod
    def valid_mark(mark):
        return 0 <= mark <= 100

    @classmethod
    def show_student_count(cls):
        print("\nTotal students:", cls.student_count)

    def display(self):
        print("Name:", self.get_name())
        print("Age:", self.get_age())
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print("Total Marks:", self.total_marks())
        print("Average:", round(self.average_marks(), 2))
        print("Grade:", self.calculate_grade())

class Sports:

    def __init__(self, sports_score):
        self.sports_score = sports_score

    def show_sports_score(self):
        print("Sports Score:", self.sports_score)

#multiple inheritance: Result class inherits from both Student and Sports classes
class Result(Student, Sports):

    def __init__(self, name, age, roll_no, marks, sports_score):
        Student.__init__(self, name, age, roll_no, marks)
        Sports.__init__(self, sports_score)

    def final_score(self):
        return self.total_marks() + self.sports_score


print("\nSTUDENT RANK LIST MANAGEMENT SYSTEM")

while True:
    try:
        n = int(input("Enter number of students: "))

        if n <= 0:
            print("Enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

students = []

for i in range(n):

    print("\nStudent", i + 1)
    print("--------------------")

    name = input("Enter name: ")

    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid age.")

    while True:
        try:
            roll_no = int(input("Enter roll number: "))
            break
        except ValueError:
            print("Please enter a valid roll number.")

    marks = []

    for j in range(3):
        while True:
            try:
                mark = int(input("Enter marks for subject " + str(j + 1) + ": "))

                if Student.valid_mark(mark):
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")

            except ValueError:
                print("Please enter a valid mark.")

    while True:
        try:
            sports_score = int(input("Enter sports score: "))

            if sports_score >= 0:
                break
            else:
                print("Sports score cannot be negative.")

        except ValueError:
            print("Please enter a valid sports score.")

    student = Result(name, age, roll_no, marks, sports_score)
    students.append(student)



print("\n\nSTUDENT DETAILS")
for student in students:
    student.display()
    student.show_sports_score()
    print("Final Score:", student.final_score())
students.sort(reverse=True)

print("\n\nRANK LIST")
rank = 1
for student in students:

    print("\nRank:", rank)
    print("Name:", student.get_name())
    print("Roll Number:", student.roll_no)
    print("Total Marks:", student.total_marks())
    print("Average:", round(student.average_marks(), 2))
    print("Grade:", student.calculate_grade())
    print("Sports Score:", student.sports_score)
    print("Final Score:", student.final_score())
    rank += 1
Student.show_student_count()
print("\nProgram completed successfully!")