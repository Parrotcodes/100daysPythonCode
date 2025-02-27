number = int(input("Enter a number: ")) 

def primeNumber(number):
    isPrime = True    
    for i in range(2,number):
        if number % i == 0:
            # isPrime = True                
            isPrime = False
    
    if isPrime:
        print("Number is prime")
    else:
        print("Number is not prime")
         
    
    
primeNumber(number)
