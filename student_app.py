student_list = []

class Student:
    def __init__(self,name):
        self.name = name
        self.marks = []

    def avg_scores(self):
        number = len(self.marks)
        if number == 0:
            return 0
        total = sum(self.marks)
        return total / number

def create_student():
    name = input("Enter student name: ")
    student_data = Student(name)  # student_data is an object.
    return student_data


def append_scores(student, mark):
    student.marks.append(mark)

def student_details(student):
    print("{}, average score: {}".format(student.name,student.avg_scores()
                                         ))

def print_student_list(students):
    for i,student in enumerate(students):
        print("ID {}".format(i))
        student_details(student)


def menu():
    selection = input("Enter 'p' to print student list,"
                      "'s' to add a new student to the list,"
                      "'a' to add he scores for the student,"
                      "'q' to exit.")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_score = int(input("Enter the score for the student: "))
            append_scores(student, new_score)
        selection = input("Enter 'p' to print student list,"
                      "'s' to add a new student to the list,"
                      "'a' to add he scores for the student,"
                      "'q' to exit.")


menu()
