students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 45},
    {"name": "Neha", "marks": 92},
    {"name": "Priya", "marks": 35},
    {"name": "Jay", "marks": 70}
]
print("student who score more than 60:")
for student in students:
    if student['marks']>=60:
        print(f"{student['name']} {student['marks']}")
        
print("calculate the Avrage Marks:")

total_marks = 0
count = 0
for student in students:
    total_marks = total_marks + student['marks']
    count +=1
    
avg_marks = total_marks/count
print(f"The Avrage Marks is {avg_marks}")

print("Find the student who have highest Marks:")
highest_marks = students[0]['marks']
for student in range(1,len(students)):
    if students[student]['marks'] > highest_marks:
        highest_marks = students[student]['marks']
print(f"The highest Marks is {highest_marks}")


print("How Many Students are passed:")
pass_student = 0
for student in students:
    if student['marks']>=40:
        pass_student +=1
print(f"The passed students count were:{pass_student}")