# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #extra bracket and int needs to be added

exam_3 = int(input("Input exam grade three: ")) #change str to int

grades = [exam_one, exam_two, exam_three] #added missing commas
sum = 0
for grade in grades: #corrected the name of the variable
  sum = sum + grade

avg = sum / len(grades) #corrected the name of the variable

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90
    letter_grade = "B"
elif avg >= 79 and avg < 80: #corrected the condition for grade C
    letter_grade = "C'
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print "Student is failing."
else:
    print "Student is passing."
