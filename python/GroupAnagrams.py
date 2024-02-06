from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        # Anagrams will be equal if we sort them, considering that we can map group anagrams to the same key in hashMap
        for w in strs:
            sortedW = "".join(sorted(w))
            if sortedW not in h:
                h[sortedW] = [w]
            else:
                h[sortedW].append(w)
        res = []

        for value in h.values():
            res.append(value)
        
        return res