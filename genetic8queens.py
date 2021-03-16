# using evolutionary algorithms to solve 8 queens problem
import itertools 
import random
from statistics import mean
import numpy as np


# heuristic is how many queens are fighting
def randomNumberSplit(N, S):
    """splits number N into S randomly split groups that sum back into N, used for random crossing-over"""

    amtLeft = N
    randomints = []

    for i in range(S):

        if i+1 == S:
            randomint = amtLeft
            randomints.append(randomint)
            break

        randomint = random.randint(0, amtLeft)
        randomints.append(randomint)
        amtLeft = amtLeft - randomint
        
    return random.sample(randomints, len(randomints))
  
def heuristic(N, listOfPositions):
    """ returns a heuristic cost that aims to be maximized . It is the amount of queens
    which are NOT in direct combat with another."""

    horizCount = 0
    # amount attacking queens in row
    for number in range(N):
        count = listOfPositions.count(number)

        if count == 0:
            pass
        elif count == 1:
            pass
        else:
            horizCount += count

        
    # for any in diagonal
    diagCount = 0
    for enum, num in enumerate(listOfPositions):

        empty = []
        for i in range(N):
            empty.append(num)
        

        updowndiag = []

        for e, n in enumerate(listOfPositions):
            diff = enum - e

            updowndiag.append(empty[i] + diff)
        

        downupdiag = []

        for e, n in enumerate(listOfPositions):
            diff = e - enum

            downupdiag.append(empty[i] + diff)
        
        newDiags = ((sum(np.array(downupdiag) == np.array(listOfPositions)) - 1) + (sum(np.array(updowndiag) == np.array(listOfPositions)) - 1))

     
        diagCount += newDiags
     
    print("diagcount", diagCount)
    return diagCount + horizCount


def makeInitialPopulation(N, amount):
    """pass in the dimension of the chessboard and the amount of initial species you would like"""
    initialPop = []

    for i in range(amount):
        newIdv = []
        for j in range(N):
            newIdv.append(random.choice(range(N)))

        initialPop.append(newIdv)
    
    return initialPop

def pairoff(N, candidates, amountofpairs, numofparents, heuristic):
    """takes a sample of the population of candidates, takes the top "amountofpairs" and pairs them into
    numofparents parents, which then recombine into amountofpairs/numofparents outputs"""
    
    queue = []
    for candidate in candidates:
        h = heuristic(N, candidate)
        queue.append(h)
    
    
    sortedCandidates = ([x for _, x in (sorted(zip(queue, candidates)))])

    k = amountofpairs*numofparents 

    sortedCandidates = sortedCandidates[:k]

    #randomly mix the sorted candidates
    candidates = random.sample(sortedCandidates, len(sortedCandidates))

    listofparents = []

    for group in range(amountofpairs):
        parents = random.sample(candidates, numofparents)
        listofparents.append(parents)

    return listofparents

def combineandcross(listofparents, numoffspring, N):
    """takes a list of parent groups, crosses them over, and returns numoffspring 
    offspring from the parent group"""

    numgroups = len(listofparents)
    numparents = len(listofparents[0])
    offspringlist = []
    
    for loop in range(numoffspring // numgroups):
        for parents in listofparents:
            offspring = crossover(parents)
            offspringlist.append(offspring)
    

    # do extras 
    for loop in range(numoffspring % numgroups):
   
        offspring = crossover(listofparents[loop])
        offspringlist.append(offspring)


    return offspringlist

import random 

def mutate(N, gene):
    possibleMutates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    for i in range(N):
 
        choice = random.choice(possibleMutates)

        if choice is not 0:
            gene[i] = random.choice(range(N))
        
        if gene[i] < 0:
            gene[i] = N + gene[i]
    
    return gene

def mutatepopulation(N, population):
    newpopulation = []
    for gene in population:
        g = mutate(N, gene)
        newpopulation.append(g)

    return newpopulation
    
            

def crossover(parents):
    """pass in a single parent group and return a single offspring, a random combination of the genes
    of the parents in blocks"""

    offspring = []
    parentnum = len(parents)
    N = len(parents[0])

    splits = randomNumberSplit(len(parents[0]), parentnum)

    for nucleotide in range(N):

        for r in range(parentnum):
            if nucleotide < sum(splits[:r+1]):
                currentparent = r
                break
        
        offspring.append(parents[currentparent][nucleotide])
    
    return offspring



def checkforsolution(N, listofgenes, hfunc):
    
    for gene in listofgenes:
        h = hfunc(N, gene)
        if h == 0:
            return gene
    
    return None


def geneticAlgorithm(N, hfunc, popsize, parentcutoff, p, stoppoint):
    """
    N: Dimension (width) of chessboard.
       hfunc: heuristic function. Must take in a single gene and return an int
       popsize: size of the initial population, and all in-between populations, at all times
       p: amount of parents for one offspring
       parentcutoff: per iteration, how many pairs should be allowed to make babies

       """ 
 
    # generate initial population
    pop = makeInitialPopulation(N, popsize)
    iterations = 0

    while True:
        
        
        # take best of the population and pair off
        bestpairs = pairoff(N, pop, parentcutoff, p, hfunc)

        
        # take best pairs, and combine and cross
        pop = combineandcross(bestpairs, popsize, N)
        # displayaverage(N, pop, heuristic)
 
        # if it is reach end, complete
        iterations += 1
        if iterations == stoppoint:
            break

        # check for solution
        a = checkforsolution(N, pop, hfunc)
        if a is not None:
            return a

            

        # mutate the population.
        pop = mutatepopulation(N, pop)
    
        
        # displayaverage(N, pop, hfunc)
    

# enter 
#solution = geneticAlgorithm(8, heuristic, 50, 8, 2, 50)
#print("possible solution:", solution)

a = heuristic(8, [4,0, 4, 7, 2, 6, 1, 3])
print(a)
