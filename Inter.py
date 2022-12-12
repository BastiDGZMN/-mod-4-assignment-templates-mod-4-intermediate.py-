def shift_letter(letter, shift):
    chosen_letter = ord(letter.upper())
    shifted = chosen_letter + shift
   
    if letter == " ":
        return letter
    
    if shifted>ord('Z'):
        shifted -= 26
                
    return chr(shifted)

letter = str(input('Enter a letter: '))
shift = int(input('How many letters do you want to shift?: '))
shifted_letter = shift_letter(letter, shift)
print(shifted_letter)


def ceaser_cipher(plain_text, shift): 
    encrypted_text = "" 
  
    for char in plain_text: 
        if char == ' ': 
            encrypted_text += char 
        elif  char.isupper(): 
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65) 
        else: 
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97) 
  
    return encrypted_text 
  
plain_text = input("Enter the string to encrypt: ")
shift = int(input("Enter the shift value: "))
  
print("Cipher Text: ", ceaser_cipher(plain_text, shift))

def shift_by_letter(letter, letter_shift):
    if letter == chr(32):
        return letter
        print(" ")
    shifted_letter = chr((ord(letter)) + (ord(letter_shift)) - 65)
    if shifted_letter > chr(90):
        new_shifted_letter =  chr((ord(letter)) + (ord(letter_shift)) - 91)
        return new_shifted_letter
        print(new_shifted_letter)
    return shifted_letter
print('SHIFT BY LETTER')
letter = str(input('Enter letter here: '))
letter_shift = str(input('Enter shift letter here: '))
shifted_letter = shift_by_letter(letter, letter_shift)
print("New letter:",shifted_letter)
################################################################################

def vigenere_cipher(message, key):
    vigenere_key = key * (len(message) // len(key))
    vigenere_key = vigenere_key + key[:len(message) % len(key)]
    return vigenere_key
def cipher(message,vigenere_key):
    encrypted_message = ''    
    for i in range(len(message)):
        if message[i] == ' ':
            encrypted_message += ' '
        else:
            shift_amount = ord(vigenere_key[i]) - ord('A')
            new_ascii = (ord(message[i]) - ord('A') + shift_amount) % 26
            encrypted_message += chr(new_ascii + ord('A'))
    return encrypted_message
message = str(input('Enter message: '))
key = str(input('Enter key: '))
vigenere_key = vigenere_cipher(message, key)
print('VIGENERE CIPHER')
print('Key phrase:', vigenere_cipher(message, key))
print('Cipher:', cipher(message,vigenere_key))