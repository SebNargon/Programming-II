print(dir(str))
print(help("hi".capitalize))
print("hello".center(50, "*"))
print("gmail.com".find("."))
s = "I see a cat who likes to cat while I cat on a cat"
# Find all occurrences
position = 0
while True:
    position = s.find("cat", position)
    if position == -1:
        break
    print(f"Found cat in position {position}")
    position += 1
    
s = "I SEE A LOT OF THINGS"
print(s.lower())

s = "I see a lot of things"
print(s.title())

s = "I see a cat"
print(s.replace("cat", "dog"))

s = "I like to go shopping"
print(s.split())


