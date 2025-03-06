# student Scores
# list of scores
# Student_Scores = [81,78,64,14,99]
# Student_Scores[1]  ---- output : 78

Student_Scores = {
    "John": 81,
    "Jane": 78,
    "Jack": 64,
    "Jill": 14,
    "Jim": 99
}

print(Student_Scores)
print(Student_Scores["Jack"])


student_grades = {}
# for i in Dictionary
# for student in Student_Scores:

for student in Student_Scores:
    # print(student)
    # print(Student_Scores[student])
    if Student_Scores[student] >= 91 and Student_Scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif Student_Scores[student] >= 81 and Student_Scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif Student_Scores[student] >= 71 and Student_Scores[student] <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
#typeconversion used beacuse we can't concatenate string and dictionary
print("Student Scores: " + str(Student_Scores)) 
print("Sutdent Grades: " + str(student_grades))