import queue

class PriorityQueue(object):
    def __init__(self):
        self.PriorityQueue = []

    def isEmpty(self):
        return len(self.PriorityQueue) == 0
    
    def insert(self, data):
        self.PriorityQueue.append(data)
    
    def get(self):      #returns and deletes current node in priority queue
        max = 0         #max is 0 because we establish that the first index of our priority queue is at 0 index
        for i in range(len(self.PriorityQueue)):
            if self.PriorityQueue[i].getFN() < self.PriorityQueue[max].getFN():
                max = i
        item = self.PriorityQueue[max]
        del self.PriorityQueue[max]
        return item
