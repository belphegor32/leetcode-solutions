from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        stack = []

        for i in range(len(position)):
            fleet.append([position[i], speed[i]])
        
        fleet = (sorted(fleet, key = lambda x: x[0]))[::-1]

        # if the car time is less than the first car, then it means that they become a single fleet and we can pop it from a stack
        for car in fleet:
            carTime = (target - car[0]) / car[1]
            stack.append(carTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)