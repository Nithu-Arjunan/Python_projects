import random

print("🎮 Welcome to Rock, Paper, Scissors!")
name = input("Enter your name")

play_again = "yes"

while play_again.lower() == "yes":

    print(f"Hello {name}!. Choose game type: \n 1. Best of 3 \n 2. Best of 5")
    game_type=int(input("Enter your choice"))

    # Set win limit
    if game_type == 1:
        win_limit = 2
    elif game_type == 2:
        win_limit = 3
    else:
        print("Invalid game type. Defaulting to Best of 3.")
        win_limit = 2

    user_score = 0
    computer_score = 0
    round_number = 1
    history = []

    def score_calculator(user_choice,computer_choice,user_score,computer_score):
        if user_choice == computer_choice:
            print("Its a tie")
            pass
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            user_score += 1
        else:
            computer_score += 1
        
        return (user_score,computer_score)

    # Main game loop
    while user_score < win_limit and computer_score < win_limit:
        print(f"🕹️ Round {round_number}")
        user_choice = (input("Choose rock, paper, or scissors")).lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"{name} chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        prev_user_score = user_score
        prev_computer_score = computer_score

        user_score,computer_score = score_calculator(user_choice,computer_choice,user_score,computer_score)

        if user_score > prev_user_score :
            print("✅ You win this round!")
            history.append(f"Round {round_number}: {user_choice} vs {computer_choice} → {name} won")
        elif computer_score > prev_computer_score :
            print("Computer wins this game")
            history.append(f"Round {round_number}: {user_choice} vs {computer_choice} → Computer won")
        else:
            
            history.append(f"Round {round_number}: {user_choice} vs {computer_choice} → Tie")
            
        print(f"Score: {name} {user_score} - Computer {computer_score}")
        round_number += 1

    # Final result

    if user_score > computer_score:
        print(f"Congratulations {name}, you won the game! 🥳")
    else:
        print("Computer won the game! Better luck next time! 🤖")


    # Print Game History
    print("\n📝 Game History:")
    for round_result in history:
        print(round_result)

    # Ask to play again
    play_again = input("\n🔁 Play again? (yes/no): ")

print(f"👋 Thanks for playing, {name}!")