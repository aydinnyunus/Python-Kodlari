import random

print(("-" * 30) + "\nRock, Paper, Scissors\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Rock\n2 - Paper\n3 - Scissors")
    user_choice = input("Your choice: ")
    computer_choice = random.choice(["1", "2", "3"])
    
    if user_choice == "1" or "Rock":
        if computer_choice == "1":
            print("Computer's choice: Rock\nRock equal to rock. Scoreless!")
            
        elif computer_choice == "2":
            print("Computer's choice: Paper\nPaper wraps stone. You lose!")
            computer_score += 100
            
        elif computer_choice == "3":
            print("Computer's choice: Scissors\nRock breaks scissors. You win!")
            user_score += 100
            
    elif user_choice == "2" or "Paper":
        if computer_choice == "1":
            print("Computer's choice: Rock\nPaper wraps stone. You win!")
            user_score += 100
            
        elif computer_choice == "2":
            print("Computer's choice: Paper\nPaper equal to paper. Scoreless!")
            
        elif computer_choice == "3":
            print("Computer's choice: Scissors\nScissors cuts paper. You lose!")
            computer_score += 100
            
    elif user_choice == "3" or "Scissors":
        if computer_choice == "1":
            print("Computer's choice: Rock\nRock breaks scissors. You lose!")
            computer_score += 100
            
        elif computer_choice == "2":
            print("Computer's choice: Paper\nScissors cuts paper. You win!")
            user_score += 100
            
        elif computer_choice == "3":
            print("Computer's choice: Scissors\nScissors equal to scissors. Scoreless!")
    
    else:
        break
    
print("\nUser's score: {}\nComputer's score: {}".format(user_score, computer_score))
