with open('input.txt') as f:
    lines = f.readlines()

# convert to 2D array with int
twoDArray = [ [int(j) for j in list(i.rstrip())] for i in lines] 

# print(twoDArray)

steps = 0
flashCounter = 0
maxSteps = 1000

cellDirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def triggerNeighborIncrease(row,col,twoDArray):

    counter = 0

    for cellDir in cellDirs:
          
        r,c = row + cellDir[0] , col + cellDir[1]

        # skip if out of bounds or flashed
        if r < 0 or c < 0 or c > (len(twoDArray[0])-1) or r > len(twoDArray)-1\
            or twoDArray[r][c] == 10:
            continue

        twoDArray[r][c] += 1 # increment the neighboring octopuses energy
        
        if twoDArray[r][c] == 10: # cell just flashed as a result of an increase
            counter += 1 + triggerNeighborIncrease(r,c,twoDArray)
        
    return counter

def prettyPrint(twoDArray):
    for i in twoDArray:
        print("".join(str(k) for k in i))

def setFlashedCellsToZeroAndReturnCount(twoDArray):
    countZeroes = 0
    for i in range(0,len(twoDArray)):
       for j in range(0,len(twoDArray[i])):
            if twoDArray[i][j] == 10: # for flashed - set the cells to zero 
               twoDArray[i][j] = 0
               countZeroes += 1

    return countZeroes

octopusCount = len(twoDArray) * len(twoDArray[0])

while steps < maxSteps:
    for i in range(0,len(twoDArray)):
        for j in range(0,len(twoDArray[i])):

            if twoDArray[i][j] != 10: # only proceed if this cell hasn't already flashed

                twoDArray[i][j] += 1

                if twoDArray[i][j] == 10:
                    # trigger neighbor increase
                    flashCounter += 1 + triggerNeighborIncrease(i,j,twoDArray)

    countZeroes = setFlashedCellsToZeroAndReturnCount(twoDArray)
     
    steps += 1
    
    if countZeroes == octopusCount:
        prettyPrint(twoDArray)
        print("Found All Zeroes at step",steps)
        break

print("Flash Counter",flashCounter)
