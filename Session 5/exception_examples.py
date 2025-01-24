name = input("What is your name? ")
print(f"Hello {name}")
age = input(f"How old are you {name}? ") # Here there can be a problem if the user enters a string
try:
    age = int(age)
    print(f"{name}, you were born in {2024-age}")
except ValueError:
    print("Please enter a valid number for age")
except:
    print("An unknown error occurred")     
else:
    print("Thank you for playing as expected")
finally:
    print("Thanks for playing!")   

