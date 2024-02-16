from typing import List
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # get the number of occurences
        count = {}
        for i in arr:
            if i in count: 
                count[i] += 1
            else: 
                count[i] = 1

        # create a minHeap, so we know which value's occurence is the smallest
        minHeap = []
        for i in count:
            minHeap.append(count[i])
        minHeap = list(minHeap)
        heapq.heapify(minHeap)

        res = len(minHeap)

        while k > 0 and minHeap:
            freq = heapq.heappop(minHeap)
            # if we can delete the value from the list, we do it, and make the result smaller by one
            if k >= freq:
                k = k - freq
                res -= 1
        
        return res
        