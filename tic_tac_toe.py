#This is tic tac toe game for two human player (does not include computer).
def sum(a,b,c):  #overriding the sum() function
    return a + b + c

def print_board(xList, oList):
    zero = "X" if xList[0] else ("O" if oList[0] else 0)   # if xList[0] gives true or false
    one = "X" if xList[1] else ("O" if oList[1] else 1)
    two = "X" if xList[2] else ("O" if oList[2] else 2)
    three = "X" if xList[3] else ("O" if oList[3] else 3)
    four = "X" if xList[4] else ("O" if oList[4] else 4)
    five = "X" if xList[5] else ("O" if oList[5] else 5)
    six = "X" if xList[6] else ("O" if oList[6] else 6)
    seven = "X" if xList[7] else ("O" if oList[7] else 7)
    eight = "X" if xList[8] else ("O" if oList[8] else 8)

    print(f" {zero} | {one} | {two}")
    print("---|---|---")
    print(f" {three} | {four} | {five}")
    print("---|---|---")
    print(f" {six} | {seven} | {eight}")

def check_winner(xList, oList):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]] #winning possibilities based on index
    for win in wins:   #win here represents the inner lists/columns
        if sum(xList[win[0]], xList[win[1]], xList[win[2]]) == 3:   #NOTE: WE have to override the sum fn. bcz it takes only two arguments
            print_board(xList, oList)
            print("X won the match!")
            return 1
        elif sum(oList[win[0]], oList[win[1]], oList[win[2]]) == 3:
            print_board(xList, oList)
            print("O won the match!")
            return 0
        
        
    return -1
        

xList = [0,0,0,0,0,0,0,0,0]
oList = [0,0,0,0,0,0,0,0,0]
print('>>>>>>>WELCOME TO THE TIC TAC TOE GAME<<<<<<<<')
print()
turn = 1   
while(True):
    print_board(xList, oList)
    if(turn % 2 != 0): 
        print("X's turn")
        value = int(input("Please enter the value: "))
        xList[value] = 1
    else:
        print("O's turn")
        value = int(input("Please enter the value: "))
        oList[value] = 1

    cwin = check_winner(xList, oList)
    if cwin != -1:
        print("Match Over!")
        break

    turn += 1
