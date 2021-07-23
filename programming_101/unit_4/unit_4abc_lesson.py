import random

while True:
    rps = ["rock", "paper", "scissors"]
    rps_hashy = { "rock": ["scissors", "paper"],
                    "paper": ["rock", "scissors"],
                    "scissors": ["paper", "rock"]}

    print("Your choices are: ")
    
    for r in rps:      
        print(f"{r}")        
    random_choice = random.choice(rps)

    users_choice = input("Make a choice, if you dare.")

    while users_choice not in rps:
        print("Your input was not correct. Try again.")
        users_choice = input("Make a choice, if you dare.") 

    print(f"The computer chose: {random_choice}")

    if random_choice == users_choice:
        print("tie")
    elif random_choice == rps_hashy[users_choice][0]:
        print("You win!")
    else:
        print("Computer wins!")

    random_number = random.randint(0,2)
    random_choice = rps[random_number]

    another_round = input("Want another go? (y/n): ")
    if another_round.lower() != "y":
        break