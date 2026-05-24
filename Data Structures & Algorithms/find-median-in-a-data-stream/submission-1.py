class MedianFinder:

    def __init__(self):
        self.minHeap = [] # large
        self.maxHeap = [] # small
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            
          
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            a = -self.maxHeap[0]
            b = self.minHeap[0]
            return (a + b) / 2.0
        
        