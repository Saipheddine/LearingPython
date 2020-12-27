import random

# programm to generate a secure passwords

print("Welcome to the PyPassword generator!")

num_letters = input("How many letters would you like in your password?")
num_symbols = input("How many symbols would you like in your password?")
num_digits = input("How many numbers would you like in your password?")

num_digits = int(num_digits)
num_letters = int(num_letters)
num_symbols = int(num_symbols)

password = ""
password_len = int(num_digits) + int(num_letters) + int(num_symbols)

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

list_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_symbols = ['*', ',', '.', '&', '%', '$', '"', '?', '=']

# add random letters to the password
for i in range(0, password_len):
    if (num_letters > 0):
        random_int = random.randint(0, len(list_letters) -1)
        num_letters -= 1
        password += list_letters[random_int]
    if (num_symbols > 0):
        random_int = random.randint(0, len(list_symbols) -1)
        num_symbols -= 1
        password += list_symbols[random_int]
    if (num_digits > 0):
        random_int = random.randint(0, len(list_digits) -1)
        num_digits -= 1
        password += str(list_digits[random_int])


print("Here is your password {}".format(password))