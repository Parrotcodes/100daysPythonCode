# nhmjo -- hello
# hello --- nhmjo

# list of alphets
alphets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

input_text = input("Enter a text: ").lower() # hello
shift_number = int(input("Enter a shift number: ")) # 4


# encry_text = "yhrlzo"
def decrpt(encrpt_text, shiftNumber):
    decry_text = ""
    for i in encrpt_text:
        position = alphets.index(i) #7 + 4 = 11
        new_position = position - shiftNumber
        decry_text  += alphets[new_position] # i = i + 4 // i += 4
    
    print(f"Your Decrypted Text: {decry_text}")




# pain_text = input_text
decrpt(input_text, shift_number) 