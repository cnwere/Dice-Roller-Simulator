import random

def roll_dice(sides=6):
    """Simulate rolling a single die with a specified number of sides (default is 6-sided)."""
    return random.randint(1, sides)

def roll_pair_of_dice():
    """Simulate rolling a pair of 6-sided dice."""
    die1 = roll_dice()  # Roll the first die
    die2 = roll_dice()  # Roll the second die
    return die1, die2

def main():
    print("Welcome to the Dice Roller Simulator!")

    while True:
        input("\nPress Enter to roll the dice...")  # Wait for user to press Enter
        die1, die2 = roll_pair_of_dice()  # Roll the dice
        total = die1 + die2

        print(f"You rolled a {die1} and a {die2} (Total: {total})")

        # Ask the user if they want to roll again
        roll_again = input("\nDo you want to roll again? (y/n): ").lower()
        if roll_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Run the dice roller simulator
main()
