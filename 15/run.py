import heapq

with open('input.txt') as f:
    lines = f.readlines()

lines = [ line.rstrip() for line in lines ]
originalW = len(lines[0])
originalH = len(lines)

def getRisk(x,y):

    count = 0

    #  transpose x back to the original data
    while x > originalW-1:
        x = x - (originalW - 1) - 1
        count += 1

    # transpose y back to the original data
    while y > originalH-1:
        y = y - (originalH - 1) - 1
        count += 1

    # get the original risk
    risk = int(lines[y][x])

    # increase risk
    nrisk = risk + count
    if nrisk > 9:
        nrisk = nrisk % 9

    return nrisk

def dijkstras(w,h):

    # Dijkstra's Algorithm
    start = (0,0)
    shortestDistFromStart = {start:0} # shortest distances from start to this position
    visited = {}  # positions of all visited cells 
    prev = {}

    #  priority queue initialized with the start and it's shortest distance
    heap = []
    heapq.heappush(heap,(0,start)) # !! important - distance is first in the tuple 

    while len(heap):
        
        minVal,index = heapq.heappop(heap)
        x,y = index

        visited[index] = True

        # get all adjacent neighors 
        neighbors =  [ (x+dx, y+dy) for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)] ]
        # that are not out of bounds
        neighbors = [ (x,y) for x,y in neighbors if x >= 0 and x < w and y >= 0 and y < h] 
        # and not already visited
        neighbors = [ neighbor for neighbor in neighbors if neighbor not in visited ]

        if shortestDistFromStart[index] < minVal: continue

        for neighbor in neighbors: 
                
            # calculate distance of this neighbor from start
            nx,ny = neighbor
            newDistance = shortestDistFromStart[index] + getRisk(nx,ny)
            # if this new distance is better or not set, set it and put this neighbor on the queue
            if neighbor not in shortestDistFromStart or newDistance < shortestDistFromStart[neighbor]:
                shortestDistFromStart[neighbor] = newDistance
                prev[neighbor] = index
                heapq.heappush(heap,(newDistance,neighbor))
    
    print(prev[(w-1,h-1)])
    return shortestDistFromStart[(w-1,h-1)]

print(dijkstras(originalW,originalH))

# adjust the width and height depending on the multiplier
w = originalW*5
h = originalH*5
print(dijkstras(w,h))


# next = []
# for i,val in enumerate(lines[0]):
#     next.append(str(getRisk(i+10,0)))


# print(lines[0])
# print("".join(next))