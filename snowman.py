from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break