# Student Report Card

english_marks = 99
math_marks = 98
science_marks = 97
hindi_marks= 96
computer_marks = 95

total_marks = english_marks + math_marks + science_marks + hindi_marks + computer_marks
percentage = (total_marks / 500) * 100
average_marks = total_marks / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print("Student Report Card")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Average Marks: {average_marks}")
print(f"Grade: {grade}")

