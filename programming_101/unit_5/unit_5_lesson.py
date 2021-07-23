import random

user_pwd_length = int(input("How many characters would you like your password to be? "))
pswd = ""
i = 0
while i < user_pwd_length:

    random_number = random.randint(33,90) 
    ascii = chr(random_number)
    pswd += ascii

    random_number = random.randint(33,90) 
    ascii = chr(random_number)
    i += 1

print(f"{pswd}")   
