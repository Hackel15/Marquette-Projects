##for x in range(5, 0, -1):
##    print(x*"*" + (10 - x*2)*" " + x*"*")
##
##
##import math
##def exp_table():
##    print("x\t" + "exp(x)")
##    print(20*"-")
##    for x in range (-5, 21):
##        print(x, "\t", math.exp(x))
##        
##exp_table()


def chess_board(x):
    for z in range(x*2):
        for _ in range (3):
            for _ in range(x):
                if(z%2==0):
                    print(5*"*"+5*" ", end="")
                else:
                    print(5*" "+5*"*", end="")
            print(end='\n')  

    
            
print("Enter an integer 'n': ", end="")
z = int(input())
chess_board(z)
    
