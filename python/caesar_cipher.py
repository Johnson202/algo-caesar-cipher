import string

def caesar_cipher(text, shift_amount):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    
    new_string = ""
    
    for i in range(len(text)):
        # handle lowercase
        if text[i] in lowercase:
            index = lowercase.index(text[i])
            new_index = (index + shift_amount) % 26
            new_string += lowercase[new_index]
        
        # handle uppercase
        elif text[i] in uppercase:
            index = uppercase.index(text[i])
            new_index = (index + shift_amount) % 26
            new_string += uppercase[new_index]
        
        else:
            new_string += text[i]
    
    return new_string

'''
# faster solution
def caesar_cipher(text, shift_amount):
    new_string = ""
    for char in text:
        if 'a' <= char <= 'z':
            # Shift lowercase letters (ASCII 97-122)
            new_string += chr((ord(char) - 97 + shift_amount) % 26 + 97)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters (ASCII 65-90)
            new_string += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            # Leave other chars alone
            new_string += char
    return new_string
'''