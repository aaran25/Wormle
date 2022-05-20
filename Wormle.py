#everything else
import random
with open("fivewords.txt",'r') as f:
    content = f.read()
tries = int("0")
guess = random.randrange(0,5718)

c = content.replace('\n', ',')
c = c.split(",")

cat = c[guess]

Dictionary = {}
for i in range (len(cat)):
    if cat[i] in Dictionary.keys():
        Dictionary[cat[i]] += 1
    else:
        Dictionary[cat[i]] = 1
while  tries < 5:
    First_Attempt = input("Your guess?")
    if First_Attempt in (c):
        tries + 1
        for i in range(len(cat)):
            if First_Attempt[i] == cat[i]:
                print("\033[1;32;20m Green\n" + First_Attempt[i])
            elif First_Attempt[i] in Dictionary.keys() and Dictionary[First_Attempt[i]] >= First_Attempt.count(First_Attempt[i]):
                print("\033[1;33;20m\n" + First_Attempt[i])
            elif guess in Dictionary:
                cat[i] in Dictionary and Dictionary[cat[i]] >= cat.count(cat[i])
            else:
                print("\033[1;30;20m\n" + First_Attempt[i])
    elif First_Attempt not in (c):
        print ("Not quite stupid. I hate to say this, but try again")
