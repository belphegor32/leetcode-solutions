from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # we will keep track of the max distance by using maxHeap
        maxHeap = []
        for i in range(len(heights) - 1):
            dif = heights[i + 1] - heights[i]
            # if we are going down, then we dont need to use bricks or ladders
            if dif <= 0:
                continue
            
            bricks -= dif
            heapq.heappush(maxHeap, dif * (-1))

            if bricks < 0:
                # if there is no bricks or ladders, that means we reached the end
                if ladders == 0:
                    return i
                # else if there is still ladders, we will use them on the max difference between building heights
                ladders -= 1
                bricks += heapq.heappop(maxHeap) * (-1)
        
        return (len(heights) - 1)