from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret_set = set([0, firstPerson])

        timeMap = {}

        for source, dest, time in meetings:
            # map all the times in the timeMap
            if time not in timeMap:
                timeMap[time] = defaultdict(list)
            
            # map source to dest and dest to source, since these are undirected edges
            timeMap[time][source].append(dest)
            timeMap[time][dest].append(source)


        def dfs(source, connections):
            if source in visit:
                return
            visit.add(source)
            secret_set.add(source)
            # run dfs on all the neighbours
            for nei in connections[source]:
                dfs(nei, connections)

        times = list(timeMap.keys())
        times.sort()

        # run dfs on all possbile times
        for time in times:
            visit = set()
            for source in timeMap[time]:
                if source in secret_set:
                    dfs(source, timeMap[time])

        return list(secret_set)