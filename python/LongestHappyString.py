from collections import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # build a max heap
        maxHeap = []
        for cnt, char in [(a, "a"), (b, "b"), (c, "c")]:
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt * (-1), char))
        
        res = ""
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            
            # if we cant append the most freq value, we take the value with the second max count
            if len(res) > 1 and char == res[-1] == res[-2]:
                if not maxHeap:
                    break
                cnt2, char2 = heapq.heappop(maxHeap)
                res += char2
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(maxHeap, (cnt2, char2))    
            else:
                res += char
                cnt += 1

            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, char))
        return res