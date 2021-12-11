with open('input.txt') as f:
    lines = f.readlines()

# read all lanternFish from feed
# lanterfish is a tuple of internalTimer and currentDay (initialized to zero)
lanternFish = [ (int(i),0) for i in lines[0].split(',') ] 

memo = {}
maxDays = 256 # 80  # part 2 and 1

def determineOffSpringCount(lanternFish):

    # use a dict to optimize
    c = memo.get(lanternFish)
    if c != None:
       return c

    (internalTimer,day) = lanternFish

    firstOffspringDay = day + internalTimer + 1 # this will be the start of our range

    if firstOffspringDay > maxDays:
        return 0

    # get all the offsprings for this lantern fish
    offSprings = [ (8,i) for i in range(firstOffspringDay,maxDays+1,7) ]

    count = len(offSprings)

    # print(lanternFish)
    # print(offSprings)

    # recursively determine the offsprings of the offsprings
    for i in offSprings:
        count += determineOffSpringCount(i)

    memo[lanternFish] = count

    return count


count = 0

for i in lanternFish:
    count += 1 + determineOffSpringCount(i) 

print(count)