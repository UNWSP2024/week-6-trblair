# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    # Sum 2 numbers
    total=dice1+dice2
    # return sum to calling function
    return total

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
dicesum=0
for x in range(1,101):
    randDice()
    dicesum=randDice()+dicesum
print(round(dicesum/100,2))
