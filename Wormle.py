#everything else
import random
with open("fivewords.txt",'r') as f:
    content = f.read()
    print(content)

#a = f.find(',' + ',')
#print(a)

guess = random.randrange(0,5719)
print(guess)


c = content.replace('\n', ',')
c = c.split(",")
print(c)
cat = c[guess]
print(cat)

First_Attempt = input("00000\n")
#Green
'''for i in range(5):
    if First_Attempt[i] == cat[i]:
        print("\033[1;32;20m Bright Green  \n")
    #In cont. Yellow
    #elif First_Attempt[i] in cat:
        dog = cat.find(First_Attempt[i])
        print(dog)
        cat = cat[0:dog] + cat[dog+1 : len(cat)]
        print(cat)


#gray
    else:
        print("\033[1;30;20m Dark Gray  \n")'''

#elif First_attempt[]





Dictionary = {"e":1}
for i in range (len(cat)):
    if cat[i] in Dictionary.keys():
        Dictionary[cat[i]] += 1
    else:
        Dictionary[cat[i]] = 1

print(Dictionary)
#ictionary[cat]



#Color code
#print("\033[1;32;40m Bright Green  \n")



