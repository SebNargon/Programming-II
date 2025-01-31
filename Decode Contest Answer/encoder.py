import random
message = input("Enter a message: ")
length = int(input("Enter the length of the rows (27 minimum): "))
if length < 27:
    length = 27
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"

with open ("secret.txt", "w") as file:
    def encode(number):
        line = ""
        positions = list(range(1, length+1))
        random.shuffle(positions)
        newpos = positions[:number]
        for i in range(1, length+1):
            if i not in newpos:
                line += (random.choice(consonant))
            elif i in newpos:
                line += (random.choice(vowel))
        file.write(line + "\n")
    
    for character in message:
        index = alphabet.find(character)
        encode(index)

            
