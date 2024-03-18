from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            cur = points[i]

            # if overlap, then we can burst to ballons at once
            if cur[0] <= prev[1]:
                res -= 1
                prev[0] = cur[0]
                prev[1] = min(prev[1], cur[1])
            # if there is no overlap we just move on
            elif cur[0] > prev[1]:
                prev = cur

        return res