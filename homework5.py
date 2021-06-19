#create a simple random add test
import random as rd

score = 0
myOper = int(input("what do you want to practice? (1. add; 2. substract; 3. multiply):        "))

d = int(input("how many questions?      "))
print(str(d) + " problems in a row!")
for i in range(int(d)):
    a = rd.randint(1, 12)
    b = rd.randint(1, 12)

    expectedResult = 0
    message = ''

    if myOper == 1:
        expectedResult = a+b
        message = "enter an answer to " + str(a) + " + " + str(b) + "  :            "
    if myOper == 2:
        expectedResult = a-b
        message = "enter an answer to " + str(a) + " - " + str(b) + "  :            "
    if myOper == 3:
        expectedResult = a*b
        message = "enter an answer to " + str(a) + " x " + str(b) + "  :            "
    c = int(input(message))
    if expectedResult == c:
        print("GREAT!")
        score = score + 100/d
        print("+" + str(100/d) + " points")
    else:
        print("NOPE!")
        print("the awnswer was " + str(expectedResult))
print("your score was.....")
print(str(score) + "%!!!")
