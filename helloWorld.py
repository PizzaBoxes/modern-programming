# input() - returns value read from stdin as valid python expression
# raw input() - returns value read from stdin as a string
# print w/o new line in Python 2: print(**, )

import random
import math

# Number Sequence

ask = input("Pick a number: ")
answer = (ask + 3) * 2 - 4 - (ask * 2) + 3

message = "The answer is " + str(answer)
print(message)

# Dice

print "Rolling..."
dice = random.choice([' ___\n| 1 |\n ---', ' ___\n| 2 |\n ---', ' ___\n| 3 |\n ---', ' ___\n| 4 |\n ---', ' ___\n| 5 |\n ---', ' ___\n| 6 |\n ---'])
dice2 = random.choice([' ___\n| 1 |\n ---', ' ___\n| 2 |\n ---', ' ___\n| 3 |\n ---', ' ___\n| 4 |\n ---', ' ___\n| 5 |\n ---', ' ___\n| 6 |\n ---'])
print dice
print dice2

# Title

hi = random.choice(['name', 'title', 'hi'])
print("This Is Called " + hi.title())

# Hypotenuse

ask1 = input("Please insert the value of leg a. ")
a = ask1
ask2 = input("Please insert the value of leg b. ")
b = ask2
c = math.sqrt((a ** 2) + (b ** 2))
print c

# 5 times table

def fiveTimesTable(endRange) :
    # Iterate over result and calculate the multiple of 5
    for i in range(0, endRange, 1) :
    # print(i*5)
        print("Five times {0} eguals {1}".format(i, 1*5))

def fiveTimesTable2():
    for table in range(0, 13):
        print(5*table)

def fiveTimesTable3():
    num = 5
    i = 0
    while(i < 6):
        i = i + 1
        print(num, "x", i, "x", num*i)
