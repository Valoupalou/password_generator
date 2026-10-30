import secrets
import string


characters_selection = string.ascii_letters + string.digits + "".join(['.','/','!','#','@'])
password = ''
is_password_standard = False
password_length_choice = False

length = int(input("Choose the length of your password (16/32/64): "))


while password_length_choice == False:

    if length != 16 and length != 32 and length != 64:
        length = int(input('You need to choose between 16, 32 or 64: '))
    else:
        password_length_choice = True

while is_password_standard == False:

    lowers_amount = 0
    uppers_amount = 0
    digits_amount = 0
    password = ""

    for i in range(length):
        password = password + secrets.choice(characters_selection)

    for c in password:

        if c.islower():
            lowers_amount += 1
        elif c.isupper():
            uppers_amount += 1
        elif c.isdigit():
            digits_amount += 1

    if lowers_amount != 0 and uppers_amount != 0 and digits_amount >= 3:
        is_password_standard = True
         

print(password)