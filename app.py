import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"\n🎲 You rolled a {die1} and a {die2}!")
    print(f"Total value: {die1 + die2}")

print("Welcome to the Dice Rolling Simulator!")

# Keep the simulation running until the user decides to quit
while True:
    choice = input("\nDo you want to roll the dice? (y/n): ").lower().strip()
    
    if choice == 'y':
        roll_dice()
    elif choice == 'n':
        print("Thanks for playing! Goodbye! 👋")
        break
    else:
        print("Invalid input! Please enter 'y' for yes or 'n' for no.")
