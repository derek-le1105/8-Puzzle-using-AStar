from puzzle import Puzzle
import search
from stack import Stack

veryEasy = [[1, 2, 3],
 [4, 5, 6],
 [7, 0, 8]]
easy = [[1, 2, 0],
 [4, 5, 3],
 [7, 8, 6]]
doable = [[0, 1, 2],
 [4, 5, 3],
 [7, 8, 6]]
oh_boy = [[8, 7, 1],
 [6, 0, 2],
 [5, 4, 3]]

generatedPuzzle = [[1, 2, 3], [7, 0, 4], [6, 5, 8]]

testCases = [veryEasy, easy, doable, oh_boy, generatedPuzzle]

def main():
    puzzle = Puzzle(getPuzzle())
    queueingFunction = getAlg()
    search.generalSearch(puzzle, queueingFunction)

def displayPuzzle(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])

def getAlg():
    algDec = int(input("Select which algorithm you want to use. '1' for Uniform Cost Search, '2' for the Misplaced Tile Heuristic, '3' for the Manhatten Distance Heuristic.: "))

    if algDec == 1:
        return search.uniformedCostSearch
    elif algDec == 2:
        return search.misplacedTile
    elif algDec == 3:
        return search.manhattenDistance
    else:
        print("not valid input")
    return

def getPuzzle():
    puzzle = []
    puzDec = int(input("Welcome to the 8-Puzzle Solver! Please press 1 to have a puzzle generated for you or 2 to create your own puzzle: "))
    if puzDec == 1:
        case = int(input("Which difficulty would you like to test? '1' for very easy, '2' for easy, '3' for doable, and '4' for difficult: "))
        if case == 1:
            puzzle = veryEasy
        elif case == 2:
            puzzle = easy
        elif case == 3:
            puzzle = doable
        elif case == 4:
            puzzle = oh_boy
        elif case == 5:
            puzzle = generatedPuzzle
    elif puzDec == 2:
        print("To enter your own puzzle, please enter valid 8 puzzles with spaces in between each number and pressing 'Enter' to submit the row")
        print("To denote an empty space in the puzzle, please use '0'. For example, 'Please enter the first row: 1 0 3'")
        rowStatus = ["first", "second", "third"]
        for i in range(len(rowStatus)):
            currRow = input(f"Please enter the {rowStatus[i]} row: ").split(" ")
            currRow = [int(x) for x in currRow]
            puzzle.append(currRow)
    print("Your puzzle is:")
    displayPuzzle(puzzle)
    return puzzle

main()