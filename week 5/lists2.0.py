student = {}

student["name"] = input("enter your name; ")
student["level"] = input("enter your level; ")
student["department"] = input("enter your department; ")
student["matric no"] = input("enter your matriculation number; ")
student["score"] = input("enter a score; ")
print()
print("student details")
print("=======================")
for key, value in student.items():
    print(f"student{key}: {value}")
