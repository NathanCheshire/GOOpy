from glob import glob
import random
import time
import functools

#TODO add tests to ensure working, once these pass, we can time it and compare to java and Go versions
#TODO use unittest to implement a TDD approach

# some tests: 
#max order of symmetric group S12 is 60 using: [3, 4, 5]
#max order of symmetric group s30 is 4620 using: [3, 4, 5, 7, 11]
#max order of symmetric group S40 is 7140 using: [1, 2, 3, 4, 5, 7, 17]

#note: computers are VERY fast, even a brute force algorithm like this doesn't take long to
#      find the max order for a group

#TODO: implement a non-brute force procedural algorithm

def main(): 
    goos = [30]

    #calculate multiple goos with a single program call
    for goo in goos:
        parts = GOObruteRandom(goo)
        print("Max order of symmetric group S", goo, " is ", int(parts[0]), " using ", parts[1], sep ='')


#driver code, copy this if you're stealing my code for your own application :P
# pls credit me though <3
def GOObruteRandom(n, timeout = 5000):
    #current maximum degree found and the cycles used to achieve it
    max = 0
    using = []

    #hold list of cycles
    global globalCycles
    globalCycles = []

    #corresponding cycle lengths (all elements multiplied together)
    productOfCycleLengths = []
    
    #start with lists of all ones from 1 to n, ex: n = 2 means ones = [[1],[1,1]]
    ones = []
    for i in range(0, n, 1):
        ones.append(1)

    #sort the base lists and add to the global cycles since these are 
    # possibilities (although unlikely) for our maximum group order
    ones.sort()
    globalCycles.append(ones)

    #add the list of just n to cycles
    nlist = [n]
    globalCycles.append(nlist)

    #generate singleton cycles of of 0 to n with the missing elements being 1's
    for i in range(n - 1, 0, -1):
        #cycle is the list of just n
        cycle = [i]

        #fill rest of available space with 1
        for j in range(0, n - i, 1):
            cycle.append(1)

        #sort the cycles and add to global list
        cycle.sort()
        globalCycles.append(cycle)
    
    #time used to end brute force process
    start = time.time() * 1000

    #if we can keep generating then do so
    while (time.time() * 1000 < start + timeout):
        cycleGenerator(globalCycles[rand(len(globalCycles) - 1)])

    #calculate the cycle lengths
    for cycle in globalCycles:
        lcm = lcmArray(cycle)
        productOfCycleLengths.append(lcm)

    #find the max cycle length and how it was achieved
    for i in range (0, len(productOfCycleLengths),1):
        lcm = productOfCycleLengths[i];
        if lcm > max:
            max = lcm
            using = globalCycles[i]

    #properly return the answer for this Goo
    return [max, using]

#finds the GOO of n using an optimal algorithm and not a brute force algorithm
#todo calculate big O runtimes for each method
def GOOoptimal(n):
    pass
    #so we can start with 1, 2, 3,... floor n/2 for an array
    #then generate relatively prime numbers to n and the first number (all other elements in array)

def GOObruteSuccessive(n):
    pass
    #our cycles list to hold all possible cycles
    cycles = []

    #all possible sizes of lists are 1 to n
    #if n = 5, singleton = {5} and list of len 5 = {1,1,1,1,1} the identity one list
    for listSize in range(1, n + 1):
        print('On lists of size: ',str(listSize),'-------------------')

        #todo make a list of all 1's here
        ones = []
        for i in range(0, listSize):
            ones.append(1)
        print(ones)

        for maxListIndex in range(1, listSize + 1):
            print('On max index: ' + str(maxListIndex),'-------------------')
            #step down from maxIndex all the way to index 0 (so first element)
            for listIndex in range(maxListIndex, 0, -1):
                for indexValue in range(listSize,0,-1):
                    #print('set index ',listIndex - 1, f' to {indexValue}')
                    sublist = ones.copy()
                    sublist[listIndex - 1] = indexValue
                    sublist.sort()

                    sum = 0
                    for index in range(0,len(sublist)):
                        sum += sublist[index]

                    if sublist not in cycles and sum == n:
                        cycles.append(sublist)

    print('Found: ', len(cycles), ' cycles')
    print(cycles)

#returns the lcm of an array
#ex: [2,13] returns 26
def lcmArray(array):
    return lcmOfArray(array, 0, len(array))

#inner lcm method used for recursion 
def lcmOfArray(array, start, end):
    if end - start == 1:
        return lcm(array[start], array[end - 1])
    else:
        return lcm(array[start], lcmOfArray(array, start + 1, end))

#finds the lcm of two integers a and b
def lcm(a, b):
    return ((a * b) / gcd(a, b))

#finds the greatest common divisor of a and b 
# this is used in the lcm method since LCM(a, b) * GCD(a, b) = a * b by Euler
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

#returns a random number between [0, max]
def rand(max):
    #can return 0,1,2,...,max - 1, max
    return random.randint(0, max)

#generates a new cycle from the provided cycle
def cycleGenerator(cycle):
    # if the size is 2 or less than stop
    if len(cycle) < 3:
        return

    #make a copy of the list
    newCycle = cycle.copy()

    #pick two random points in the list
    r1 = rand(len(cycle) - 1)
    r2 = rand(len(cycle) - 1)

    #add the points
    sum = newCycle[r1] + newCycle[r2]

    #set the first point to the sum
    newCycle[r1] = sum

    #remove the second point from the list
    del newCycle[r2]

    #sort the list
    newCycle.sort()

    #add to global cycles if not already in it
    if newCycle not in globalCycles:
        globalCycles.append(newCycle)

if __name__ == '__main__':
    GOObruteSuccessive(5)