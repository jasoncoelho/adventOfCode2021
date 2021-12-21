with open('input.txt') as f:
    lines = f.readlines()

lines = [ line.rstrip() for line in lines ]

calledNumbers = lines[0].split(',')

# dict number to x,y
def generatelookup(board):
    d = {}
    for i in range(0,len(board)):
        for j,val in enumerate(board[i]):
            d[val] = (i,j)
    return d

boards = []

board = [] 
for i in lines[2:]:
    if len(i) == 0:
        boards.append((generatelookup(board),set()))
        board = []
        continue
    board.append(i.split())
boards.append((generatelookup(board),set()))

def processAndCheckIfWon(board,calledNumber):

    lookup,marked = board

    if calledNumber in lookup:

        x,y = lookup[calledNumber]
        marked.add((x,y))

        columnWin = len([ 1 for posY in range(0,5) if (x,posY) in marked ]) == 5
        rowWin = len([ 1 for posX in range(0,5) if (posX,y) in marked ]) == 5

        if columnWin or rowWin:
            return (True,sum([ int(i) for i in lookup if lookup[i] not in marked]))

    return (False,None)

won = False

wonBoards = []
wonCalledNumbers = []

for calledNumber in calledNumbers:

    for board in [b for b in boards if b not in wonBoards]:

        won,unmarkedSum = processAndCheckIfWon(board,calledNumber)
        
        if won:
            wonBoards.append(board)
            wonCalledNumbers.append((unmarkedSum,calledNumber))
 
unmarkedSum, winningNumber = wonCalledNumbers[0]
print("first winning solution solution = ", unmarkedSum * int(winningNumber))            
           
unmarkedSum, winningNumber = wonCalledNumbers[len(wonCalledNumbers)-1]
print("last winning solution solution = ", unmarkedSum * int(winningNumber))

# first winning solution solution =  4662
# last winning solution solution =  12080