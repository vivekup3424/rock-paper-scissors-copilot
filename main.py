#implement rock, paper,scissors game
#1. Display tilte of the game
#1. player should be given prompt ("What do want to choose: \"Rocl\", \"Paper\", \"Scissors\"");
#2. import random module and computer should be given random choice
#3. After all this display the result in the form of an winning or losing animation
#4. If the user has enter wrong input then display "You have entered wrong input"
#5. At last ask user if he/she wants to play again or not
#6. If user wants to play again then repeat the game else exit the game
import random
import time

def display_title():
    print("Welcome to Rock, Paper, Scissors!")

def get_user_choice():
    return input("What do you want to choose: \"Rock\", \"Paper\", or \"Scissors\": ").strip().lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def display_result(user_choice, computer_choice):
    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")

    time.sleep(0.5)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")

def play_again():
    return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

def main():
    display_title()
    play_game = True

    while play_game:
        user_choice = get_user_choice()

        if user_choice in ["rock", "paper", "scissors"]:
            computer_choice = get_computer_choice()
            display_result(user_choice, computer_choice)
        else:
            print("You have entered wrong input. Please choose either \"Rock\", \"Paper\", or \"Scissors\".")

        play_game = play_again()

    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
