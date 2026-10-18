import random

def roll_dice():
    # Generate two random numbers between 1 and 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    print(f"🎲 You rolled a {die1} and a {die2}!")
    print(f"Total value: {die1 + die2}")

# Run the function
print("Welcome to the Dice Rolling Simulator!")
roll_dice()
