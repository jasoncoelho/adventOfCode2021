with open('input.txt') as f:
    lines = f.readlines()

# representing the graph as a map
graph = {}

for line in [ i.rstrip() for i in lines]:
    pointA , pointB = line.split("-")
    for a,b in [(pointA,pointB),(pointB,pointA)]:
        # these should only appear on one side of the map
        if a != "end" and b != "start": 
            if a not in graph:
                graph[a] = []
            graph[a].append(b)

print(graph)

def travel(presentCave,smallCavesTravelled):

    count = 0

    if presentCave == "end":
        return 1

    if presentCave.islower():
        smallCavesTravelled.append(presentCave)

    for caveChoice in graph[presentCave]:
        if caveChoice not in smallCavesTravelled:
            count += travel(caveChoice,smallCavesTravelled.copy())

    return count

def travelOneSmallCaveTwice(presentCave,smallCavesTravelled,smallCaveTravelledTwice):

    c = 0

    if presentCave == "end":
        return 1

    if presentCave.islower():
        if presentCave in smallCavesTravelled:
            smallCaveTravelledTwice.append(presentCave)
        else:
            smallCavesTravelled.append(presentCave)

    for caveChoice in graph[presentCave]:
       
        if caveChoice not in smallCavesTravelled or\
            (caveChoice in smallCavesTravelled and len(smallCaveTravelledTwice) == 0):
            c += travelOneSmallCaveTwice(caveChoice,smallCavesTravelled.copy(),
                    smallCaveTravelledTwice.copy())

    return c

countSolution1 = 0
countSolution2 = 0

for a in graph['start']:
    # print("Start")
    countSolution1 += travel(a,[])
    countSolution2 += travelOneSmallCaveTwice(a,[],[])

print("solution 1",countSolution1)
print("solution 2",countSolution2)