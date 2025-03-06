# Nesting of Dictionary inside Dictionary
# Nesting of List inside Dictionary
# Nesting of Dictionary inside List

# Nesting of Dictionary inside Dictionary


# without nesting
dictioanry1 = {
     "Key1": "Value1",
    "Key2": "Value2",    
}

# with nesting of dictionary inside dictionary
dictioanry2 = {              #if 
    "Key0": "value",            # stmt1
     "Key1": 
            {                   #if    
             "Key11":"Value11",    #stmt2
             "Key12":"Value12"     #stmt3
             },
    "Key2": 
            {                   #if
            "Key21":"value21",    #stmt4
            "Key22":"value22"     #stmt5
            },    
}

for key in dictioanry2:
    print(key)
    
    
print(dictioanry2["Key1"])
print(dictioanry2["Key1"]["Key11"])

# for i in range(1,3):
#     for j in range(1,3):
#         print(i,j)   



# # Nesting of Dictionary inside List

# # without nesting
# list1 = ["Value1","Value2","Value3"]

# # with nesting of List inside Dictionary
# student_info = {
#     [],
#     [],
#     [],
# }

student_info = {
    "name": "John",
    "age": 25,
    "subejcts": ["Telugu","Hindi","English","Maths","Science","Social"], # nested list accournding dictionary
    "marks": [90,80,70,60,50,40],
    "subjectwiseMarks": {  # nested dictionary
        "Telugu": 90,
        "Hindi": 80,
        "English": 70,
        "Maths": 60,
        "Science": 50,
        "Social": 40
    }
}

# print(student_info["subejcts"])

# for subject in student_info:
    # print(subject)

for subject in student_info["subjects"]:
    print(subject)

for marks in student_info["marks"]:
    print(marks)
    
