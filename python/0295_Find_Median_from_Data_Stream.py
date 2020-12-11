import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.count += 1
        heapq.heappush(self.max_heap,(-num,num))
        _,max_heap_top=heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,max_heap_top)

        if self.count&1:
            min_heap_top=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,(-min_heap_top,min_heap_top))

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count&1:
            return self.max_heap[0][1]
        else:
            return (self.min_heap[0]+self.max_heap[0][1])/2