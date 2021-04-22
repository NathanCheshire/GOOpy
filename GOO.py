import math
import random
import time
import functools
import collections

#the goos you want to compute, you can have multiple
goos = [15]
globalCycles = []
msPerGoo = 5000

#tests to ensure working, once these pass, we can time it and compare to java
#TODO use unittest to implement a TDD approach
#max order of symmetric group S12 is 60 using: [3, 4, 5]
#max order of symmetric group S40 is 7140 using: [1, 2, 3, 4, 5, 7, 17]

#note: computers are VERY fast, even a brute force algorithm like this doesn't take long to
#      find the max order for a group

#TODO: implement a non-brute force procedural algorithm

def main(): 
    for goo in goos:
        parts = GOObrute(goo)
        print("Max order of symmetric group S", goo, " is ", int(parts[0]), " using ", parts[1], sep ='')

#driver code, copy this if you're stealing my code for your own application :P
# pls credit me though <3
def GOObrute(n):
    max = 0
    using = []
    globalCycles = []
    productOfCycleLengths = []

    ones = []
    for i in range(0, n, 1):
        ones.append(1)

    ones.sort()
    globalCycles.append(ones)

    nlist = [n]
    globalCycles.append(nlist)

    for i in range(n - 1, 0, -1):
        cycle = [i]

        for j in range(0, n - i, 1):
            cycle.append(1)

        cycle.sort()
        globalCycles.append(cycle)
    
    start = time.time() * 1000

    while (time.time() * 1000 < start + msPerGoo):
        cycleGenerator(globalCycles[rand(len(globalCycles) - 1)])


    for cycle in globalCycles:
        productOfCycleLengths.append(lcmArray(cycle))

    for i in range (0, len(productOfCycleLengths),1):
        if productOfCycleLengths[i] > max:
            max = productOfCycleLengths[i]
            using = globalCycles[i]

    return [max, using]

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

#TODO make generator

@functools.lru_cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def cycleGenerator(cycle):
    if len(cycle) < 3:
        return
    newCycle = cycle.copy()
    r1 = rand(len(cycle) - 1)
    r2 = rand(len(cycle) - 1)
    sum = newCycle[r1] + newCycle[r2]
    newCycle[r1] = sum
    del newCycle[r2]
    newCycle.sort()
    if any(list != cycle for list in globalCycles):
        #ERROR not getting added
        print("add") 
        globalCycles.append(cycle)

main()