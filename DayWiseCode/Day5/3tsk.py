# Instructions:
# Don't use the sum() and len() functions to calculate the average height of the students.
# Don't use the max() and min() functions to calculate the highest score in the class.

# Task:
# Average height of students
# sum() and len() are built-in functions in Python. They are used to calculate the sum and length of a list, respectively.


# Task:
# Highest Score in the class
# max() and min() are built-in functions in Python. They are used to calculate the maximum and minimum values in a list, respectively.




















# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
student_scores_input = input("Enter the student scores: ").split()

for n in range(0,len(student_scores_input)):
    student_scores_input[n] = int(student_scores_input[n])

print(student_scores_input)

heighest_score = 0
for highest in student_scores_input:
    if highest > heighest_score:
        heighest_score = highest

print(f"The highest score in the class is: {heighest_score}")