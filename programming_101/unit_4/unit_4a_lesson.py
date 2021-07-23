import random
while True:
# Declare an array with the options to choose
    rps = ["rock", "paper", "scissors"]
    print("Your choices are: ")
    for r in rps:
        
        print(f"{r}")
    
    # Establish a random int between 0-2 corresponding to the index of rps
    
    random_number = random.randint(0,2)
   
    # Define a random choice by plugging in the index randomly generated just previously to rps
    
    random_choice = rps[random_number]

    # begin a loop to display the choices, then ask the user to choose one

    users_choice = input("Make a choice, if you dare.")
    print(f"The computer chose: {random_choice}")

    # Logic to see if you have won
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
# Making sure the input was valid
    else:
        print("Your input was not correct. Try again.")

# Grabbing another random number 
    random_number = random.randint(0,2)
    random_choice = rps[random_number]
# Wanna go again?
    another_round = input("Want another go? (y/n): ")
    if another_round.lower() != "y":
        break