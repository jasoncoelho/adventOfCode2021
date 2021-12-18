with open('input.txt') as f:
    lines = f.readlines()

lines = [ line.rstrip().split(' ') for line in lines ]

# convert the commands into tuples of direction and distance
commands = [ (l[0],int(l[1])) for l in lines ]

def partA():

    currentPos = (0,0)

    for direction,dist in commands:
        x,y = { 'down' : (0,1) , 'forward' : (1,0) , 'up' : (0,-1) }[direction]
        currentPos = (currentPos[0] + (x*dist), currentPos[1] + (y*dist)) # move
        print(currentPos)

    return currentPos

def partB():

    currentPos = (0,0)
    aim = 0

    for direction,dist in commands:
        aim = aim + { 'down': dist , 'up' : -1 * dist , 'forward' : 0}[direction]
        if direction == 'forward':
            currentPos = (currentPos[0]+dist,currentPos[1]+(aim*dist))

    return currentPos

def printSolution(solution):
    horizontalPosition, depth = solution
    print('PART A')
    print('depth', depth, 'horizontal pos',horizontalPosition)
    print('multiplication',depth*horizontalPosition)

printSolution(partA())
printSolution(partB())