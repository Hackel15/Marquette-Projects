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
    
