#everything else
import random
with open("fivewords.txt",'r') as f:
    content = f.read()
    print(content)

#a = f.find(',' + ',')
#print(a)

guess = random.randrange(0,5724)
print(guess)


c = content.replace('\n', ',')
c = c.split(",")
print(c)
cat = c[guess]
print(cat)

First_Attempt = input("00000\n")
#Green
for i in range(5):
    if First_Attempt[i] == cat[i]:
        print(("\033[1;32;20m Bright Green  \n"))
    #In cont. Yellow
    elif First_Attempt[i] != cat[i]:
        for i in range(5):
#gray
    else:
        print(("\033[1;30;20m Dark Gray  \n"))








#Color code
