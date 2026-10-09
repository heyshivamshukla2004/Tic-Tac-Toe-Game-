import numpy as np 
board = np.zeros( (3,3),dtype=int)
print(board)
def print_board(b):
    symbols=  {0:"", 1:"X",  -1:"0"}
    for i in range (3):
        row = "   | ".join(symbols[val] for val in b[i])
        print(" " + row)
        if i<2:
            print("---+---+---")
print()

def check_winner(b):
    if 3 in np.sum(b,axis=1)or 3 in np.sum(b,axis = 0 ):
        return 'X'
    if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis = 0 ):
        return'O'           
    # trace is for sum of diagonal 
    #  fliplr is use for flip the  array air matrix 
    if np.trace(b) == 3 or np.trace(np.fliplr(b))==3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b))== -3 :
        return "O"
    if not 0 in b:
        return "DRAW"
    return None
current =1
print("Welcome to Tic Tac Toe ")
print_board(board)
while True :
    if current ==1:
        player = 'X'
    else:
        player = 'O'

    try:
        row = int(input(player+"- Enter row(0,1,2)"))
        col = int (input(player+ "- Enter column (0,1,2)"))
    except ValueError:
        print("please enter numbers only \n")
        continue 
    if row<0 or row>2 or col<0 or col>2 :
        print("row and coloumn  must be between 0 and 2 ")
        continue
    if board[row,col] !=0:
        print("cell is alreday taken ")
        continue
    board[row,col]=current 
    print_board(board)
    result =check_winner(board)
    if result is not None :
        if result =="DRAW":
            print("ohoo its draw")
        else :
            print(result,"WINS")
        break
    if current ==1:
        current = -1 
    else:
        current= 1


    