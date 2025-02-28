# Encrption and Decryption of text using Caesar Cipher

# list of alphets
alphets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

# plain_text = "hello"
def encrpt(plain_text, shiftNumber):
    encry_text = ""
    for i in plain_text:
        position = alphets.index(i) #7 + 4 = 11
        new_position = position + shiftNumber
        encry_text  += alphets[new_position] # i = i + 4 // i += 4
    
    print(f"Your Encrpted Text: {encry_text}")


# encry_text = "yhrlzo"
def decrpt(encrpt_text, shiftNumber):
    decry_text = ""
    for i in encrpt_text:
        position = alphets.index(i) #7 + 4 = 11
        new_position = position - shiftNumber
        decry_text  += alphets[new_position] # i = i + 4 // i += 4
    
    print(f"Your Decrypted Text: {decry_text}")
    

repeat = True
ask_agin = input("Start Encryption or decryption Game by typing 'yes' : " ).lower()
 
while repeat:
    type_your_choice = input('Type "encode" to Encrpt the text or "decode" to Decrpt the text : ').lower()
    input_text = input("Enter a text: ").lower() # hello
    shift_number = int(input("Enter a shift number: ")) # 4
    
    if type_your_choice == "encode":
        encrpt(input_text, shift_number)
    elif type_your_choice == "decode":
        decrpt(input_text, shift_number)
    else:
        print("Invalid Input")
    
    ask_agin = input("Do you want to continue? Type 'yes' or 'no' : ").lower()
    
    if ask_agin == "no":
        repeat = False
        print("Thank you for using our service")