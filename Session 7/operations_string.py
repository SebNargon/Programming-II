s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(f"{s1} {s2}")
print(s1, s2)
print(3 * (s1 + " "))
print(s1, len(s1))
print(3 * s2, len(3 * s2))
for c in s2:
    print(c)
    
new = ""    
for c in s1:
    new += (4 * c)
    
for c in s2:
    print(4 * c, end="")
    
# in can be used to check if one string is in another
print("h" in s1)
print("d" in s2)
print(s1 in s1) 


# counter = 0
# for i in counter:
#     if s1[counter] = s2[counter]:
#         print("same")
#     else:
#         print(f"s"")

