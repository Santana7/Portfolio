from random import randint
money=int(input("How much money are you starting with?"))

bet=int(input("How much money do you want to bet?"))

color = ["red", "black"]
choose = input ("Guess a color.")

roll = color[randint(0,1)]

if choose == roll:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("correct")
    money = money + bet
else:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("wrong")
    money = money - bet

from random import randint
parity = ["odd", "even"]
choose = input ("Odd or even?")

roll = parity[randint(0,1)]

if choose == roll:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("correct")
    money = money + bet
else:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("wrong")
    money = money - bet

from random import randint
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
choose = input ("Choose a number")

roll = parity[randint(1,37)]

if choose == roll:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("correct")
    money = money + bet
else:
    print("ball roll:"+ str(roll))
    print("your roll:" +str(choose))
    print("wrong")
    money = money - bet

print("Your balance:")
print(money)