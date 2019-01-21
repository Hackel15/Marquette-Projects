import random
def guessing_game():
    total = 0
    rand = random.randint(0, 100)
    my_guess = guess()
    total+=1
    check_guess(my_guess, rand)
    while (my_guess != rand):
        my_guess = guess()
        total+=1
        check_guess(my_guess, rand)
    print("Random #:",rand,", Total guesses:", total) 
        

def guess():
    print("Enter guess: ", end="")
    return int(input())

def check_guess(x, y):
    if x < y:
        print("TOO LOW")
    elif x > y:
        print("TOO HIGH")
    else:
        print("CORRECT GUESS! YOU WIN!")
    
