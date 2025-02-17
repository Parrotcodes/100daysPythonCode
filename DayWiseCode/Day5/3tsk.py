# Instructions:
# Don't use the sum() and len() functions to calculate the average height of the students.
# Don't use the max() and min() functions to calculate the highest score in the class.

# Task:
# Average height of students
# sum() and len() are built-in functions in Python. They are used to calculate the sum and length of a list, respectively.


# Task:
# Highest Score in the class
# max() and min() are built-in functions in Python. They are used to calculate the maximum and minimum values in a list, respectively.



# student_scores = [78, 65, 89, 86, 55, 91, 64, 18]
# Instrunction:
#  1. values shouled be inserted by the user (using input() method)
#  2. Change those inserted values into list and display the list of items
#  3. Now try to find the highest value from the inserted list items
student_scores_input = input("Enter the student scores: ").split()

for n in range(0,len(student_scores_input)):
    student_scores_input[n] = int(student_scores_input[n])

print(student_scores_input)



