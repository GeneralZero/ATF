import string

first = raw_input("Please enter Plaintext to Cipher: ")
k = int(raw_input("Please enter the shift: "))

shifted_lowercase = string.ascii_lowercase[k:] + string.ascii_lowercase[:k]
translation_table = string.maketrans(string.ascii_lowercase, shifted_lowercase)

print first.translate(translation_table)
