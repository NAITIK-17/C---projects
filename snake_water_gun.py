#Snake Water gun game
import random
def play_game():
    user_score = 0
    computer_cscore = 0
    choices = ["Snake", "Water", "Gun"]
    while True:
        user_choice = input("Enter your choice (Snake/water/gun): ").capitalize()
        if user_choice not in choices:
            print("Invalid choice! PLease choose from snake water gun")
            return play_game()
        computer_choice = random.choice(choices)
        print(f"Computer choice: {computer_choice}")
        print(f"Your choice: {user_choice}")
        if user_choice == computer_choice:
            print("It's a tie")
        elif (user_choice == "SNAKE" and computer_choice == 'WATER')or\
            (user_choice == "WATER" and computer_choice == "GUN")or\
            (user_choice == 'GUN' and computer_choice == "SNAKE"):
            print("You win!")
            user_score += 1
        elif user_choice == "q":
            print("Thanks for playing !")
            break
        else:
            print("You lose!")
            computer_cscore += 1
        print(f"Your score: {user_score}, Computer score: {computer_cscore}")

