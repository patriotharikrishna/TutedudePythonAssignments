
student_marks = {
    "Hari": 85,
    "Krishna": 92,
    "Manish": 78,
    "Modi": 88,
}

print("Available Students:")
for name in student_marks.keys():
    print(f"  - {name}")

print("\n" + "="*40)

student_name = input("\nEnter a student's name: ").strip()

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"Marks for {student_name}: {marks}")
else:
    print(f"Error: '{student_name}' not found in the student records.")
    print("Please check the name and try again.")
