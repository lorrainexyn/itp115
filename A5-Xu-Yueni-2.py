# Yueni Xu, yuenixu@usc.edu
# ITP 115, Spring 2021
# Assignment 5
# Description:
# D20 Dice Game
import random
def main():
    # 20 sides dice
    # played 10 times (for loop)
    #randomly generate a number


    outcome = False
    points = 0

    for i in range(1, 11):
        caseNum = random.randrange(1, 6, 1)
        diceNum = random.randrange(1, 21, 1)
        print("\nYou are playing for CASE",caseNum)
        print("You will win for the following numbers:")
        if caseNum == 1:
            for h in range(2,22,2):
                print(h," ", end="")
                if diceNum == h:
                    outcome = True



        elif caseNum == 2:
            for u in range(1,21,2):
                print(u," ", end="")
                if diceNum == u:
                    outcome = True




        elif caseNum == 3:
            for z in range(5,11,1):
                if diceNum == z:
                    outcome = True
                print(z, " ", end="")



        elif caseNum == 4:
            for o in range(10,22,2):
                print(o, " ", end="")
                if diceNum == o:
                    outcome = True



        elif caseNum == 5:
            for y in range(3,21,3):
                print(y," ", end="")
                if diceNum == y:
                    outcome = True



        print()
        print("\nNow rolling...")
        print("You rolled a", str(diceNum) + "!")

        if outcome == True:
            print("You won 50 points!:)\n")
            points = points + 50
        elif outcome == False:
            print("You didn't win:(\n")



    print ("Your total score is:", points)
    print("Thanks for playing!")



# if the roll matches the current number from the range



main()

