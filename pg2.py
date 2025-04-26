import random
choices = ["rock", "paper", "scissors"]
def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: "). lower()
        if user_choice in choices:
            return user_choice
        else:
            print(" Invalid choice. Please choose rock, paper, or scissors.")
def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
(user == "paper" and computer == "rock") or \
(user == "scissors" and computer == "paper"):
        return " You win!"
    else:
        return "You lose!"
def play_game():
 user_score = 0
computer_score = 0
while True:
    print("\n Rock, Paper, Scissors - Let's Play!")
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice} \nComputer chose: {computer_choice}")
    result = get_winner(user_choice, computer_choice)
    print (result)
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
        print(f"\n Score - You: {user_score} | Computer: {computer_score}")
        play_again = input("\n Play again? (yes/no): ").strip() . lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break
        if __name__ == "__main__":
            play_game()