import random
import math

words = ['a',
         'b',
         'c',
         'd',
         'e',
         'f',
         'g',
         'h',
         'i',
         'j',
         'k',
         'l',
         'm',
         'n',
         'o',
         'p',
         'q',
         'r',
         's',
         't',
         'u',
         'v',
         'w',
         'x',
         'y',
         'z',
         '1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '0',
         '-',
         '_',
         '.']
length = None
while True:
    try:
        length = int(input("Enter the number of characters in the password: "))
        break
    except ValueError:
        continue

password = ""

for i in range(length):
    CaseRandom = math.floor(random.random() * 2)
    WordRandom = math.floor(random.random() * (len(words) - 1))
    if CaseRandom == 0:
        if type(words[WordRandom]) != int:
            password = password + words[WordRandom].upper()
        else:
            password = password + words[WordRandom]
    else:
        password = password + words[WordRandom]
print(password)
input("")
