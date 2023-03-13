students= ["dilek","mücahit"]
def get_student():
    while True:
        student = input("Enter the name and surname of the student: ")
        if not student:
            print("Please enter a non-empty name.")
            continue
        students.append(student)
        ask = input("Do you want to add another student? (yes/no): ").lower()
        if ask == "no":
            break
    print("Students have been added to the list.")
def remove_student(student):
    for s in students:
        if student==s:
            students.remove(s)
            print("student has been removed from list.")
def remove_multiple_students():
    while True:
        student = input("Enter the name of the student you want to remove: ")
        students.remove(student)
        ask = input("Do you want to remove another student? (yes/no): ").lower()
        if ask == "no":
            break
    print("Students have been removed from the list.")
def show_students(students):
    for student in students:
        print(student)
def find_student_id(students):
    for id,student in enumerate(students):
        print(id,student)
show_students(students)