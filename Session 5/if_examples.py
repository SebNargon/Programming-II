# Let's create a virtual bartender that serves you if you are of legal age
from random import choice
drinks = ["beer", "wine", "whiskey", "vodka", "gin", "rum", "tequila", "brandy", "cognac", "absinthe"]
mixers = ["coke", "tonic", "soda", "orange juice", "cranberry juice", "lemonade", "lime juice", "ginger ale", "cola", "sprite"]
name = input("What should I call you? ")
try:
    age = int(input(f"How old are you {name}? ")) # This is where the problem can occur
    legal = None
    country = input(f"Where are you from, {name}? ").lower()
    if age < 14:
        legal = False
    elif age < 16:
        if country == "austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "austria" or country == "germany" or country == "luxembourg" or country == "spain":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "usa" or country == "uae":
            legal = False
        else:
            legal = True
    else:
        legal = True
        
    if legal:
        suggestion = f"{choice(drinks)} {choice(mixers)}"   
        print(f"I suggest you try a {suggestion}.")
        drink = input("Would you like to try it? Otherwise, let me know what you want! ")
        if drink.lower() == "yes":
            print(f"Here you go, {name}! Enjoy your suggestion!")
        else:
            print(f"One {drink} coming right up, {name}!")
    if not legal:
        suggestion = f"{choice(mixers)}"
        drink = input(f"I'm sorry, but I can't serve you alcohol. Would you like a {choice(mixers)} instead? Otherwise, let me know what you want! ")
        if drink.lower() == "yes":
            print(f"Here you go, {name}! Enjoy your {suggestion}!")
        else:
            print(f"One {drink.lower()} coming right up, {name}!")
except ValueError:
    print("I don't have time for your games. Get out")
