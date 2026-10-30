import secrets
import string


class Generator:

    characters_selection = string.ascii_letters + string.digits + "".join(['.','/','!','#','@'])
    is_password_standard = False
    password_length_choice = False

    def __init__(self, length):

        self.length = length

    def generating_password(self):

        while self.is_password_standard == False:

            lowers_amount = 0
            uppers_amount = 0
            digits_amount = 0
            password = ""

            for i in range(int(self.length)):
                password = password + secrets.choice(self.characters_selection)

            for c in password:

                if c.islower():
                    lowers_amount += 1
                elif c.isupper():
                    uppers_amount += 1
                elif c.isdigit():
                    digits_amount += 1

            if lowers_amount != 0 and uppers_amount != 0 and digits_amount >= 3:
                self.is_password_standard = True

        return password


"""while password_length_choice == False:

    if length != 16 and length != 32 and length != 64:
        length = int(input('You need to choose between 16, 32 or 64: '))
    else:
        password_length_choice = True"""