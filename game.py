import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize scores
user_score = 0
computer_score = 0

# Main game loop
while True:
    # Prompt the user to choose
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer's random choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    # Update the score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Score -> You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
