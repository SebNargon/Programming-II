fp = open("text.txt", "r")
print(fp.read())
fp.close()

#Same thing, but more pythonic

with open("text.txt", "r") as fp:
    print(fp.read())
print("We are done, the context closed by the indent")

with open("text.txt", "r") as fp:
    linenum = 1
    for line in fp:
        #print(line, end="")
        print(f"{linenum}: {line.rstrip()}")
        linenum += 1
        

        