with open('input.txt') as f:
    lines = f.readlines()

vents = set()       # vent coordinates
overlapped = set()  # vent coordinates that have overlapped atleast twice

def coordinate(x,y):
    # return str(x) + ":" + str(y)
    return ( x , y )

def getAllVentCoordinates(point1,point2):
    
    point1x,point1y = [ int(i) for i in point1.split(",") ]
    point2x,point2y = [ int(i) for i in point2.split(",") ]

    print(point1,point2)

    if point1x == point2x : # x co-ordinates are the same hence vertical line
        start, end = sorted([ point1y, point2y ])
        return  { coordinate(point1x,i) for i in range(start,end+1) }
    elif point1y == point2y : # y co-ordinates are the same hence horizontal line
        start, end = sorted([ point1x, point2x ])
        return  { coordinate(i,point1y) for i in range(start,end+1) } 
    else: # diagonal lines
        xDir = 1 if point1x < point2x else -1
        yDir = 1 if point1y < point2y else -1
        ret =  { coordinate(point1x + (i*xDir), point1y + (i*yDir))  for i in range(0, abs(point1x - point2x) + 1) }
        return ret


# Using for loop
for i in lines:
    
    point1,point2 = i.replace('\n','').split(" -> ")
    ventCoordinates = getAllVentCoordinates(point1,point2)

    # print(ventCoordinates)

    if len(ventCoordinates) != 0:

        if len(vents) == 0:
            vents = ventCoordinates # initialize if first time generating co-ordinates
        else:
            for i in ventCoordinates:
                if i in vents:         # if it already exists
                    vents.remove(i)    # move it to the overlapped set
                    overlapped.add(i)
                elif i not in overlapped:
                    vents.add(i)       # otherwise add it to the set of vents

print(len(overlapped))