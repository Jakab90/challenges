import random


def valid(grade_entered):
    return grade_entered > -1 and grade_entered < 101

go_again = "y"

while go_again == "y":

    grade_entered = int(input("Enter a grade between 0 and 100"))
    modded = grade_entered % 10
    if not(valid(grade_entered)):
        print("Invalid input, try again.")

    elif grade_entered >= 90: 
        if modded > 5 or grade_entered == 100:
            print("A+")
        elif modded < 5:
            print("A-")
        else:
            print("A")
    elif grade_entered >= 80:
        if modded > 5:
            print("B+")
        elif modded < 5:
            print("B-")
        else:
            print("B")
    elif grade_entered >= 70:
        if modded > 5:
                print("C+")
        elif modded < 5:
            print("C-")
        else:
            print("C")
    elif grade_entered >= 60: 
        if modded > 5:
                print("D+")
        elif modded < 5:
            print("D-")
        else:
            print("D")
    else: 
        print("F")
    
    rival_score = random.randint(50,100)

    if (grade_entered < rival_score) & valid(grade_entered):
        print("You scored lower than your rival")
    elif grade_entered == rival_score & valid(grade_entered):
        print("Wow! You and your rival are neck and neck")
    elif valid(grade_entered):
        print("Congratulations! You smashed your competition")
    print(f"Rival score: {rival_score}")
    go_again = input("want to enter another grade? (y/n): ")
