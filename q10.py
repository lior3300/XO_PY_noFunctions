import random

# presenting the rules
print('''this is a tic-tac-toe game.
there are 2 players (one is X other is O) and a grid of 3X3.
the goals of the players is to fill a line/column/diagonal with their symbol (X or O).
X is starting, a random value of True or False will be chosen, if True been chosen you are x and you'll start.\n''')

winner=None
turn=bool(random.getrandbits(1))
if turn:
    player=" X "
    computer=" O "
else:
    player=" O "
    computer=" X "
print("the value is True you're X and go first\n") if turn else print("the value is False you're O and go second\n")

board=[
        [f" {0+line//2*3} ","|",f" {1+line//2*3} ","|",f" {2+line//2*3} "] if line%2==0 
        else ["---","+","---","+","---"]
        for line in range(5)
    ]
freeSpaces=[i for i in range(9)] #list of free positions on the board, used by computer to choose randomly

pturns=0 #turns that were played
while pturns<9:
    # displaying the board
    for line in board:
        print(*line)
    #if it's the users turn
    if turn:
        print("the free positions are:",*freeSpaces)
        choice=int(input("choose a position: "))

        board[2*(choice//3)][2*(choice%3)]=player #set in the board player
        freeSpaces.remove(choice)
        pturns+=1
        print(f"you chose: {choice}\n")
    else:
        choice=int(random.choice(freeSpaces))
        
        board[2*(choice//3)][2*(choice%3)]=computer #set in the board computer
        freeSpaces.remove(choice)
        pturns+=1
        print(f"computer chose: {choice}\n")
    
    #search for winner
    for i in range(3):
        if board[2*i][0]==board[2*i][2]==board[2*i][4]: #check line
            winner=1
            break
        elif board[0][2*i]==board[2][2*i]==board[4][2*i]: #check column
            winner=1
            break
    if board[0][0]==board[2][2]==board[4][4] or board[0][4]==board[2][2]==board[4][0]: #check diagonals
        winner=1

    if winner: #if someone won set the winner
        if turn:
            winner=player 
        else:
            winner=computer 
        break

    turn=not turn #switch turns

if winner: #if winner is not None print the winner
    print(f"{winner} has won!")
else:
    print("a tie!")