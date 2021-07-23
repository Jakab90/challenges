import random
rps = ["rock", "paper", "scissors"]

random_number = random.randint(0,2)
random_choice = rps[random_number]

users_choice = input("Choose one: rock, paper, scissors")

if random_choice == users_choice:
    print("tie")
elif users_choice == rps[0]:
    if random_choice == rps[1]:
        print("Computer wins!")
    else:
        print("You win!")
elif users_choice == rps[1]:
    if random_choice == rps[0]:
        print("You win!")
    else:
        print("Computer wins!")
elif users_choice == rps[2]:
    if random_choice == rps[0]:
        print("Computer wins!")
    else:
        print("You win!")   
print(f"Computer chose: {random_choice}")


