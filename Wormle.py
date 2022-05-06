#everything else
import random
with open("fivewords.txt",'r') as f:
    content = f.read()

guess = random.randrange(0,5718)

c = content.replace('\n', ',')
c = c.split(",")

cat = c[guess]
print(cat)


Dictionary = {}
for i in range (len(cat)):
    if cat[i] in Dictionary.keys():
        Dictionary[cat[i]] += 1
    else:
        Dictionary[cat[i]] = 1
for i in range(5):
    First_Attempt = input("Your guess?")
    for i in range(1):
        for i in range(len(cat)):
            if First_Attempt[i] == cat[i]:
                print("\033[1;32;20m Green  \n")
            elif First_Attempt[i] in Dictionary.keys() and Dictionary[First_Attempt[i]] >= First_Attempt.count(First_Attempt[i]):
                print("\033[1;33;20m Yellow\n")
            elif guess in Dictionary:
                cat[i] in Dictionary and Dictionary[cat[i]] >= cat.count(cat[i])
            else:
                print("\033[1;30;20m Gray \n")


