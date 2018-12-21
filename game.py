from random import randint
n=1
while( n !=0):
    player = input("enter paper(p),scissor(s),rock(r) ? >>")
    comp = randint(1,3)
# 1 == rock
# 2 == scissor
# 3 == paper
    if(player == 'p' ):
        if(comp == 1):
            print("computer: rock")
            print("hurre! you won the match")
        if (comp == 2):
            print("computer: scissor")
            print(" oh! you lost this time")
        if (comp == 3):
            print("computer: paper")
            print(" This goes to draw")

    if(player == 'r' ):
        if(comp == 1):
            print("computer: rock")
            print(" This goes to draw")

        if (comp == 2):
            print("computer: scissor")
            print(" hurre! you won the match")

        if (comp == 3):
            print("computer: paper")
            print(" oh! you lost this time")


    if(player == 's' ):
        if(comp == 1):
            print("computer: rock")
            print(" oh! you lost this time")

        if (comp == 2):
            print("computer : scissor")
            print("This goes to draw")

        if (comp == 3):
            print("computer: paper")
            print("hurre! you won the match")


    n = input("if u want to exit  enter 0 otherwise any int.")
