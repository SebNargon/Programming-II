with open("journal.txt", "a") as journal:
    while True:
        text = input("Enter your journal entry: (press q to quit): ")
        if text == "q":
            break
        journal.write(text.capitalize() + "\n")
        