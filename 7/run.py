import math
from numpy import array, abs, sum, median, mean

with open('input.txt') as f:
    lines = f.readlines()

crabSubs = array([ int(i) for i in  lines[0].split(',') ])

print(crabSubs)

# fuel consumption at 1 

medianSub = round(median(crabSubs))

print("Median" , medianSub)
print("Part 1 " , sum([ abs(medianSub - i) for i in crabSubs ]))

# fuel consumption incremental by 1 every 1 move

meanSub = mean(crabSubs)
meanSubFloor =  math.floor(meanSub)
meanSubCeil = math.ceil(meanSub)

print("Mean Floor",meanSubFloor)
print("Mean Ceil", meanSubCeil)

def calculateFuel(r):
    return sum([ i for i in range(1,r+1)])

meanSubFuelFloor  = sum([ calculateFuel(i) for i in  abs(array(crabSubs) - meanSubFloor) ])
meanSubFuelCeil  = sum([ calculateFuel(i) for i in  abs(array(crabSubs) - meanSubCeil)  ])

print("Part 2 " , min(meanSubFuelFloor,meanSubFuelCeil))