import random

characters = "1234567890qwertyuioplkjhgfdsazxcvbnm`~!@#$%^&*()-_=+[{]}\|';:/?.>,<"

password = ''

for x in range(16):
    password += random.choice(characters)

print_password = f"Your Password:  {password} "

print(print_password)
