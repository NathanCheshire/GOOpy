import math
import random
import time

#list of lists of cycle lengths
cycles = []
currentN = 0

#timeout for each goo
msPerGoo = 1000

#the goos you want to compute, you can have multiple
goos = [12,40]


#note: computers are VERY fast, even a brute force algorithm like this doesn't take long to
#      find the max order for a group

#TODO: implement a non-brute force procedural algorithm

def main(): 
    for goo in goos:
        parts = GOO(goo)
        print("Max order of symmetric group S", goo, " is ", int(parts[0]), " using ", parts[1], sep ='')

#driver code, copy this if you're stealing my code for your own application :P
# pls credit me though <3
def GOO(n):
    max = 0
    using = []
    cycles = []
    productOfCycleLengths = []

    ones = []
    for i in range(0, n):
        ones.append(1)
    
    ones.sort()
    cycles.append(ones)

    nList = []
    nList.append(n)
    nList.sort()
    cycles.append(nList)

    i = n - 1
    while i > 0:
        cycle = []
        cycle.append(i)

        j = 0
        while j < n - i:
            cycle.append(1)
            j += 1

        cycle.sort()
        cycles.append(cycle)
        i -= 1
    
    currentCycle = []
    start = round(time.time() * 1000)

    while round(time.time() * 1000) <= start + msPerGoo:
        cycleGenerator(cycles[rand(len(cycles) - 1)])

    for cycle in cycles:
        productOfCycleLengths.append(lcmArray(cycle))

    i = 0
    while i < len(productOfCycleLengths):
        if productOfCycleLengths[i] > max:
            max = productOfCycleLengths[i]
            using = cycles[i]
        i += 1

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
    return random.randint(0, max)

def cycleGenerator(cycle):
    if (len(cycle) < 3):
        return 0;
    
    newCycle = cycle
    r1 = rand(len(newCycle) - 1)
    r2 = rand(len(newCycle) - 1)
    sum = newCycle[r1] + newCycle[r2]
    newCycle[r1] = sum
    del newCycle[r2]
    newCycle.sort()
    if (newCycle not in cycles):
        cycles.append(newCycle)

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

main()