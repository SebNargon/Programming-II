# You have 3 lives. I roll a dice, if I roll 6, you win. If not a 6, you lose 1 life
from random import randint
lives = 3
while lives:
    roll = randint(1, 6)
    pause = input("Ready? ")
    if roll == 6:
        print("You rolled a 6. You win!")
        break
    else: # This can be removed and unindented, but is kept for clarity
        lives -= 1
        print(f"You rolled a {roll}. You have {lives} left.")
else:
    print("You lost all your lives. Game over!")