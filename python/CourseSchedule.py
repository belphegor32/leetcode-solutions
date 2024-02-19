from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {x: [] for x in range(numCourses)}

        # map all the courses to its prerequisites
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        # add a set to detect a cycle
        visit = set()
        def dfs(crsInd):
            # if the crs with this index is already in the set, it means we are visiting it second time, so its a cycle
            if crsInd in visit: 
                return False
            # if the course prerequisites is an empty list, it means we met conditions to take the course, so we can continue dfs
            if prereqMap[crsInd] == []:
                return True
            
    
            visit.add(crsInd)
            # check all prerequisited, if any of them lead to a cycle, we return False
            for pre in prereqMap[crsInd]:
                if dfs(pre) == False:
                    return False
            
            visit.remove(crsInd)
            prereqMap[crsInd] = []
            return True
        
        # check all starting positions, and if any lead to a cycle, we immidiately return False
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        # if there are no cycles and we can take all courses, we return
        return True