import math
import random
import time
import functools
import collections

#the goos you want to compute, you can have multiple
goos = [12,40]

#max order of symmetric group S12 is 60 using: [3, 4, 5]
#max order of symmetric group S40 is 7140 using: [1, 2, 3, 4, 5, 7, 17]

#note: computers are VERY fast, even a brute force algorithm like this doesn't take long to
#      find the max order for a group

#TODO: implement a non-brute force procedural algorithm

def main(): 
    for goo in goos:
        parts = GOO(goo)
        #print("Max order of symmetric group S", goo, " is ", int(parts[0]), " using ", parts[1], sep ='')

#driver code, copy this if you're stealing my code for your own application :P
# pls credit me though <3
def GOO(n):
    max = 0
    using = []
    globalCycles = []
    productOfCycleLengths = []

    #add to global cycles using procedural algorithm if generated sorted cycle is not in globalCycles

    for i in range(1, n, 1):
        currentCycle = [i]
        for i in range(0, n - i, 1):
            currentCycle.append(1)

        globalCycles.append(currentCycle)
        print("here")

        if len(currentCycle) > 3:
            firstCopy = currentCycle.copy()
            sum = firstCopy[0] + firstCopy[1]
            firstCopy[0] = sum
            del firstCopy[1]
            globalCycles.append(firstCopy)

            lastCopy = currentCycle.copy()
            sum = lastCopy[-1] + lastCopy[-2]
            lastCopy[-1] = sum
            del lastCopy[-2]
            globalCycles.append(lastCopy)

            middleCopy = currentCycle.copy()
            sum = middleCopy[math.floor(len(currentCycle) / 2.0)] + middleCopy[math.floor(len(currentCycle) / 2.0) + 1]
            middleCopy[math.floor(len(currentCycle) / 2.0)] = sum
            del middleCopy[math.floor(len(currentCycle) / 2.0) + 1]
            globalCycles.append(middleCopy)
            
            return 0
        elif len(currentCycle == 2):
            sum = currentCycle[0] + currentCycle[1]
            currentCycle[0] = sum
            del currentCycle[1]
            globalCycles.append(currentCycle)
    print(len(globalCycles))

    for cycle in globalCycles:
        productOfCycleLengths.append(lcmArray(cycle))

    for i in range (0, len(productOfCycleLengths),1):
        if productOfCycleLengths[i] > max:
            max = productOfCycleLengths[i]
            using = globalCycles[i]

    return [max, using]

#no convert intergers here since we're using python :D

#outer lcm method
def lcmArray(array):
    return lcmOfArray(array, 0, len(array))

#inner lcm method
def lcmOfArray(array, start, end):
    if end - start == 1:
        return lcm(array[start], array[end - 1])
    else:
        return lcm(array[start], lcmOfArray(array, start + 1, end))

def lcm(a, b):
    return ((a * b) / gcd(a, b))

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
def rand(max):
    #can return 0,1,2,...,max - 1, max
    return random.randint(0, max)


@functools.lru_cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

main()