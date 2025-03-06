# calculator 


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def NewCalculation():
    first_number = int(input("What is the first number? "))
    second_number = int(input("What is the second number? "))

    for key in operations:
        print(key)
        
    pic_operation = input("Pick an operation: ") 
    calcuation = operations[pic_operation]
    result = calcuation(first_number,second_number)

    print(f"Your final solution {first_number} {pic_operation} {second_number} is {result}")

    continue_caluation = False

    while not continue_caluation:
        next_cal = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start a new calculation: ")

        if next_cal == 'y':
           first_number = result
        else:
            continue_caluation = True
            NewCalculation()




NewCalculation()
