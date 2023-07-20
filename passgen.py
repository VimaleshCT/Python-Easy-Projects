import random
import string

len = int(input("Enter length of password:"))

print(''' 
        1.Digits
        2.Letters
        3.Punctuations
        4.Exit  ''')

chac = ""

while (True):
    choice = int(input("pick a number:"))
    if choice == 1:
        chac += string.digits
    elif choice == 2:
        chac += string.ascii_letters
    elif choice == 3:
        chac += string.punctuation
    elif choice == 4:
        break
    else:
        print("please select the valid option ")
        break;

password = []

for i in range(len):
     random_pass = random.choice(chac)
     password.append(random_pass)
     





print("Random password is:".join(password))
