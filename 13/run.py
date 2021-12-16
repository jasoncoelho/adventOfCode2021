with open('input.txt') as f:
    lines = f.readlines()

# read the input and get the coordinates and folds
lines = [ i.rstrip() for i in lines ]
coordinates = [ i.split(",") for i in lines if not i.startswith("fold") and len(i)]
coordinates = { (int(k[0]),int(k[1])) for k in coordinates }
                     
folds = [ i.replace("fold along ","").split("=") for i in lines if i.startswith("fold") and len(i)]
folds = [ ( k[0], int(k[1]) ) for k in folds ]

def transpose(fold,x,y,foldAxis):
    
    if foldAxis == 'x' and x > fold:
        newX = fold - (x - fold)
        return (newX,y)
    elif foldAxis == 'y' and y > fold:
        newY = fold - (y - fold)
        return (x,newY)
    else:
        return (x,y)

lastFoldX,lastFoldY = 0,0
print(folds)
count = 1
for foldAxis,fold in folds:
    if foldAxis == 'x':
        lastFoldX = fold 
    if foldAxis == 'y':
        lastFoldY = fold
    coordinates = { transpose(fold,x,y,foldAxis) for (x,y) in coordinates }
    print( "count",count,"dots visible",len(coordinates),fold,foldAxis)
    count += 1

c = list(coordinates)
c.sort()
print(c)

print(lastFoldX,lastFoldY)

# flipped this since the output appears to be a mirror image
for y in range(0,lastFoldY):
    line = []
    for x in range(0,lastFoldX):
        if (x,y) in coordinates:
            line.append('#')
        else:
            line.append(' ')
    print("".join(line))