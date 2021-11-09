import numpy as np
import copy                                                     #use copy library to deepcopy puzzle list without referencing original list when making copies 
from priorityQueue import PriorityQueue                         #we use our implemented priorityqueue data structure as the DS for our nodes 
from node import Node
from stack import Stack                                         #we use our implemented stack data structure to print out the solution path 

goalPuzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
repeatedPuzzles = []
expandedNodes = 0

def generalSearch(puzzle, queueingFunction):       #puzzle is the puzzle class that contains our initial puzzle, queueingFunction is the function we'll use for searching
    nodes = PriorityQueue()
    initState = Node(puzzle.problem)
    nodes = queueingFunction(nodes, [initState])        #places inital state into priority queue, as well as getting and setting values for f(n), g(n), and h(n)
    repeatedPuzzles.append(puzzle.problem)                 #place initial puzzle into repeatedPuzzles
    maxQueueSize = 0

    while not nodes.isEmpty():
        node = nodes.get()                          #gets element in the priorityQueue DS (pops items like in a stack)
        node.maxQueueSize = maxQueueSize
        node.numExpandedNodes = expandedNodes
        if isGoalState(node):
            solPath = Stack()
            getSolutionPath(node, solPath)
            while not solPath.isEmpty():
                solutionNodes = solPath.pop()
                print(f"Optimal state to expand with g(n) of {solutionNodes.getGN()} and h(n) of {solutionNodes.getHN()} is: ")
                printTable(solutionNodes.data)
            
            print("Goal State!")
            print(f"Solution depth was {node.depth}")
            print(f"Number of nodes expanded was {expandedNodes}")
            print(f"Max queue size was {maxQueueSize}")
        else:
            nodes = queueingFunction(nodes, expand(node, puzzle.getOperators(node.data)))       
            if len(nodes.PriorityQueue) > maxQueueSize:
                maxQueueSize = len(nodes.PriorityQueue)

def printTable(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])

def expand(puzzle, puzzleOps):      #puzzleOps is a list that contains all possible operators for the blank space '0' excluding repeated states
    expandedChildren = []
    opsToRemove = []
    global expandedNodes            #without this, we get error about undefined local variable despite being defined above
    for i in range(len(puzzle.data)):
            for j in range(len(puzzle.data)):
                if puzzle.data[i][j] == 0:
                    blankRow, blankCol = i, j
                    break
    
    for op in puzzleOps:
        puzzleCopy = copy.deepcopy(puzzle.data)             #makes a copy of puzzle.data without referring to original data so we can manipulate and append to expandedChildren
        if op == 'Up':
            tileToSwap = puzzleCopy[blankRow - 1][blankCol]
            puzzleCopy[blankRow][blankCol] = tileToSwap
            puzzleCopy[blankRow-1][blankCol] = 0
        elif op == 'Left':
            tileToSwap = puzzleCopy[blankRow][blankCol - 1]
            puzzleCopy[blankRow][blankCol] = tileToSwap
            puzzleCopy[blankRow][blankCol - 1] = 0
        elif op == 'Right':
            tileToSwap = puzzleCopy[blankRow][blankCol + 1]
            puzzleCopy[blankRow][blankCol] = tileToSwap
            puzzleCopy[blankRow][blankCol + 1] = 0
        elif op == 'Down':
            tileToSwap = puzzleCopy[blankRow + 1][blankCol]
            puzzleCopy[blankRow][blankCol] = tileToSwap
            puzzleCopy[blankRow+1][blankCol] = 0

        if not isRepeated(puzzleCopy):                  #checks to see if the new copied, manipulated data is a repeated state
            repeatedPuzzles.append(puzzleCopy)          #if puzzleCopy is not repeated, add to repeatedPuzzles list so program can look out for this puzzle as well
            tempNode = Node(puzzleCopy)                 #we do this so if we encounter the state again, we dont expand it since we already expanded that state once
            tempNode.setDepth(puzzle.getDepth() + 1)
            expandedChildren.append(tempNode)
        else:
            opsToRemove.append(op)            #if a state is repeated, we dont add to tree so it wont be expanded

    if len(opsToRemove) != 4:               #if we dont remove all operators, we can still expand current puzzle
        expandedNodes += 1
    for badOp in opsToRemove:
        puzzleOps.remove(badOp)
    
    puzzle.insertIntoTree(puzzle, puzzleOps, expandedChildren)          #insert into tree structure so we know what solution path is later
    return expandedChildren

def isRepeated(puzzle):
    repeatedFound = False
    for state in repeatedPuzzles:
        if np.array_equal(puzzle, state):  #a repeated state is found
            return True
        else:   #no repeated states detected
            repeatedFound = False
    return repeatedFound

def isGoalState(puzzle):
    if np.array_equal(puzzle.data, goalPuzzle):
        return True
    else:
        return False

def uniformedCostSearch(nodes, expandedChildren):       #nodes is priority queue DS, expandedChilderen is a list of Nodes
    tempQueue = nodes
    for child in expandedChildren:
        child.setGN(child.getDepth())
        child.setFN()
        tempQueue.insert(child)
    return tempQueue       

def misplacedTile(nodes, expandedChildren):
    tempQueue = nodes
    indexList = [[0, 0], [0, 1], [0, 2],            #used to replace nested for loop as nested for loops will add our run time
                 [1, 0], [1, 1], [1, 2],
                 [2, 0], [2, 1], [2, 2]]
    
    for child in expandedChildren:
        numOfMisplacedTiles = 0
        for index in indexList:
            i, j = index
            if (child.data[i][j] != goalPuzzle[i][j]) and (child.data[i][j] != 0):
                numOfMisplacedTiles +=1     #this becomes our heuristic
        child.setGN(child.getDepth())
        child.setHN(numOfMisplacedTiles)
        child.setFN()
        tempQueue.insert(child)
    return tempQueue

def manhattanDistance(nodes, expandedChildren):
    tempQueue = nodes
    indexList = [[0, 0], [0, 1], [0, 2],
                 [1, 0], [1, 1], [1, 2],
                 [2, 0], [2, 1], [2, 2]]

    for child in expandedChildren:
        totalDistance = 0
        for index in indexList:
            i, j = index
            if (child.data[i][j] != goalPuzzle[i][j]) and (child.data[i][j] != 0):      #if current tile is not correct AND is not a blank tile
                a, b = indexList[child.data[i][j] - 1]
                totalDistance += (abs(a - i) + abs(b-j))
                """for a in range(len(child.data)):             over time, run time grows exceedingly bc of nested for loop
                    for b in range(len(child.data)):            use indexList and find the tile we want; this dramatically reduces our run time
                        if(child.data[i][j] == goalPuzzle[a][b]):
                            totalDistance += (abs(a - i) + abs(b - j))"""

        child.setGN(child.getDepth())
        child.setHN(totalDistance)
        child.setFN()
        tempQueue.insert(child)

    return tempQueue

def getSolutionPath(goalState, solutionPath):           
    while goalState.parent != None:         
        solutionPath.push(goalState)        #we use stack DS so the first node we meet(goal state), becomes the last node we end up print (LIFO)
        goalState = goalState.parent        #set new goalState to the parent so we traverse the tree and only get the path
    if goalState.parent == None:
        solutionPath.push(goalState)        #if no parent, we have reached root node
    return
