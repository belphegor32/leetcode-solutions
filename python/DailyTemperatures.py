from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resArr = [0] * len(temperatures)
        stack = []

        # iterate thru the list, add values to a stack until the higher temp is not met, then update res if higher one is found
        # we use a monotonicly decreasing stack, since its a very efficient way to solve the problem
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                stackT, stackI = stack.pop()
                resArr[stackI] = i - stackI

            stack.append([temperatures[i], i])
        
        return resArr
            