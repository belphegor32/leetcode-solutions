from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if the size of array cant be divided with remainder 0, then return False, since we cant create groups
        if len(hand) % groupSize != 0:
            return False
        
        # counter hashMap for all values in hand
        countMap = {}

        for i in hand:
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1

        # minHeap to check the least freq element
        minHeap = list(countMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            top = minHeap[0]

            # check all the numbers stating from top of heap up to the last consequative element that needsto be in the group
            for i in range(top, top + groupSize):
                # if the elem is not in hashMap, that means we cant make a group
                if i not in countMap:
                    return False
                countMap[i] -= 1
                # we can only pop the value from heap if its the least frequent
                if countMap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True