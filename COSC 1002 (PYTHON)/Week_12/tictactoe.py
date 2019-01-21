class TicTacToe:
    def __init__(self):
        self.posX = []
        self.posO = []
        
    def __str__(self):
        mapping = [ [" " for j in range(3)] for i in range(3)]
        for pos in self.posX:
            i, j = pos
            mapping[i][j] = "X"
        for pos in self.posO:
            i, j = pos
            mapping[i][j] = "O"
        print(mapping)
        return (5*"-"+"\n""|"+
            "|\n|".join(["".join(mapping[i]) for i in range(3)])+
            "|\n"+5*"-")
    
    def translate(answer):
        if answer == 1:
            return (0,0)
        if answer == 2:
            return (0,1)
        if answer == 3:
            return (0,2)
        if answer == 4:
            return (1,0)
        if answer == 5:
            return (1,1)
        if answer == 6:
            return (1,2)
        if answer == 7:
            return (2,0)
        if answer == 8:
            return (2,1)
        if answer == 9:
            return (2,2)

    def getMoveX(self):
        while True:
            answer = input("Enter move for x by entering a number between 1 and 9  ")
            try:
                answer = int(answer)
            except ValueError:
                print("You need to return an integer")
                continue
            if answer < 1 or answer > 9:
                print("You need to return an integer between 1 and 9")
                continue
            pos = TicTacToe.translate(answer)
            if pos in self.posX:
                print("The position is not open")
                continue
            if pos in self.posO:
                print("Your opponent already marked that spot")
                continue
            return pos
        
    def getMoveO(self):
        while True:
            answer = input("Enter move for o by entering a number between 1 and 9  ")
            try:
                answer = int(answer)
            except ValueError:
                print("You need to return an integer")
                continue
            if answer < 1 or answer > 9:
                print("You need to return an integer between 1 and 9")
                continue
            pos = TicTacToe.translate(answer)
            if pos in self.posO:
                print("The position is not open")
                continue
            if pos in self.posX:
                print("Your opponent already marked that spot")
                continue
            return pos
        
    def checkDone(lista):
        for i in range(3):
            if (i,0) in lista and (i,1) in lista and (i,2) in lista:
                return True
        for j in range(3):
            if (0,i) in lista and (1,i) in lista and (2,i) in lista:
                return True
        if (0,0) in lista and (1,1) in lista and (2,2) in lista:
            return True
        if (0,2) in lista and (1,1) in lista and (2,0) in lista:
            return True 

    def explain():
        print(
        """Mark the fields using an integer between 1 and 9
                  1  2  3
                  4  5  6
                  7  8  9""")

    def play(self):
        TicTacToe.explain()
        turnX = True
        while len(self.posX)+len(self.posO) < 9:
            if turnX:
                self.posX.append(self.getMoveX())
                if TicTacToe.checkDone(self.posX):
                    print(self)
                    print("X has won")
                    return
            else:
                self.posO.append(self.getMoveO())
                if TicTacToe.checkDone(self.posO):
                    print(self)
                    print("O has won")
                    return
            turnX = not turnX
            print(self)
        print("It's a tie")
                
            
        




ttt = TicTacToe()
ttt.play()


        
            
