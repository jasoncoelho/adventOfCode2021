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
        boards.append((generatelookup(board),{}))
        board = []
        continue
    board.append(i.split())
boards.append((generatelookup(board),{}))

# print("len boards",len(boards))
# print("boards",boards)
# print("called number",calledNumbers)

def processAndCheckIfWon(board,calledNumber):

    lookup,marked = board

    if calledNumber in lookup:

        x,y = lookup[calledNumber]
        marked[(x,y)] = calledNumber

        columnWin = len([ 1 for posY in range(0,5) if (x,posY) in marked ]) == 5
        rowWin = len([ 1 for posX in range(0,5) if (posX,y) in marked ]) == 5

        if columnWin or rowWin:
            return (True,sum([ int(i) for i in lookup if i not in marked.values()]))

    return (False,None)


wonFirst = False
latestWinningNumber = None 
won = False
latestUnmarkedSum = None

wonBoards = []

for calledNumber in calledNumbers:

    for board in [b for b in boards if b not in wonBoards]:

        won,unmarkedSum = processAndCheckIfWon(board,calledNumber)

        if won:
            wonBoards.append(board)
            print("winning called number", calledNumber)
            latestWinningNumber = calledNumber
            latestUnmarkedSum = unmarkedSum
            if not wonFirst:
                print("winning board", board,"\n at number",latestWinningNumber)
                print("unmarked sum = ", unmarkedSum)
                print("solution = ", unmarkedSum * int(latestWinningNumber))
                wonFirst = True
            
           
print("last winning board", board,"\n at winning number",latestWinningNumber)
print("last winining unmarked sum = ", latestUnmarkedSum)
print("last winning solution solution = ", latestUnmarkedSum * int(latestWinningNumber))