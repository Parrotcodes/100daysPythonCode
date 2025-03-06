# hello --- nhmjo

# list of alphets
alphets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

input_text = input("Enter a text: ").lower() # hello
shift_number = int(input("Enter a shift number: ")) # 4


# plain_text = "hello"
def encrpt(plain_text, shiftNumber):
    encry_text = ""
    for i in plain_text:
        position = alphets.index(i) #7 + 4 = 11
        new_position = position + shiftNumber
        encry_text  += alphets[new_position] # i = i + 4 // i += 4
    
    print(f"Your Encrpted Text: {encry_text}")


# pain_text = input_text
encrpt(input_text, shift_number) 