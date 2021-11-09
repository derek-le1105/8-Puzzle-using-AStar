class Puzzle:
    def __init__(self, data):
        self.problem = data

    def getBlankSpace(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == 0:
                    return i, j

    def getOperators(self, puzzle):     #gets the available operators of the blank space    
        opList = []         

        blankRow, blankCol = self.getBlankSpace(puzzle)

        if blankRow == 0:           #order is left, right, up, down    ULRD
            if blankCol == 0:
                opList.append('Right')
                opList.append('Down')
            elif blankCol == 1:
                opList.append('Left')
                opList.append('Right')
                opList.append('Down')
            elif blankCol == 2:
                opList.append('Left')
                opList.append('Down')
        elif blankRow == 1:
            if blankCol == 0:
                opList.append('Right')
                opList.append('Up')
                opList.append('Down')
            elif blankCol == 1:
                opList.append('Up')
                opList.append('Left')
                opList.append('Right')
                opList.append('Down')
            elif blankCol == 2:
                opList.append('Up')
                opList.append('Left')
                opList.append('Down')
        elif blankRow == 2:
            if blankCol == 0:
                opList.append('Up')
                opList.append('Right')
            elif blankCol == 1:
                opList.append('Up')
                opList.append('Left')
                opList.append('Right')
            elif blankCol == 2:
                opList.append('Up')
                opList.append('Left')
        return opList
