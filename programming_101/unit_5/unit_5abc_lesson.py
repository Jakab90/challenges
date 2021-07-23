import random
import string

pswd = ""
i = 0   

while True:
    
    letter_length = (input("How many letters would you like? Choose a whole number between 1-100: "))
    number_length = (input("How many numbers would you like? Choose a whole number between 1-100: "))
    special_length = (input("How many special characters would you like? Choose a whole number between 1-100: "))

    try:
       val_one = int(letter_length)
       val_two = int(number_length)
       val_three = int(special_length)
       break
    
    except ValueError:
       print("Please enter a number next time!")

letter_length = int(letter_length)
number_length = int(number_length)
special_length = int(special_length)

while i < (letter_length)/2:
    random_number = random.randint(65,90)
    ascii = chr(random_number)
    pswd += ascii
    i += 1
letter_length -= i

i = 0

while i < letter_length:
    random_number = random.randint(97, 122) 
    ascii = chr(random_number)
    pswd += ascii
    i += 1
i = 0

while i < number_length:
    random_number = random.randint(48, 57) 
    ascii = chr(random_number)
    pswd += ascii
    i += 1
i = 0

while i < special_length:
    random_number = random.randint(33,38) 
    ascii = chr(random_number)
    pswd += ascii
    i += 1

shuffled = ''.join(random.sample(pswd, len(pswd)))

print(f"Your new password is:\n{shuffled}")


'''
import random
import string

i = 0
sentence = ""
user_letter = int(input("Letters?"))
while i < (user_letter)/2:
    ran_up = random.choice(string.ascii_uppercase)
    sentence += butt
    i +=1
user_letter -= i

i = 0

while i < user_letter:
    ran_low = random.choice(string.ascii_lowercase)
    sentence += butts
    i += 1
i = 0
print(sentence)
'''