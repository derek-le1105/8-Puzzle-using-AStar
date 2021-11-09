class Node:
    def __init__(self, data):
        self.data = data
        self.gN = 0
        self.hN = 0
        self.fN = 0
        self.depth = 0
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.parent = None
        self.maxQueueSize = 0
        self.numExpandedNodes = 0

    #accessors
    def getGN(self):
        return self.gN

    def getHN(self):
        return self.hN

    def getFN(self):
        return self.fN

    def getDepth(self):
        return self.depth

    #setters
    def setGN(self, newGN):
        self.gN = newGN

    def setHN(self, newHN):
        self.hN = newHN

    def setFN(self):
        self.fN = self.getGN() + self.getHN()

    def setDepth(self, newDepth):
        self.depth = newDepth

    #tree methods
    def insertIntoTree(self, parent, puzzleOps, expandedChildren):
        for op in puzzleOps:
            if op == 'Left':
                self.left = expandedChildren[puzzleOps.index('Left')]
                self.left.parent = parent
            elif op == 'Right':
                self.right = expandedChildren[puzzleOps.index('Right')]
                self.right.parent = parent
            elif op == 'Up':
                self.up = expandedChildren[puzzleOps.index('Up')]
                self.up.parent = parent
            elif op == 'Down':
                self.down = expandedChildren[puzzleOps.index('Down')]
                self.down.parent = parent
        return

    

    