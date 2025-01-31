alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
counter = 0
with open("new_message.txt") as f:
    for line in f:
        for item in line:
            if item in vowel:
                counter += 1
        message += alphabet[counter]
        counter = 0
print(message)

