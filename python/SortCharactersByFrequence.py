class Solution:

    # A bucket sort algorithm, map each char to frequence and then multiply the char by its frequence
    def frequencySort(self, s: str) -> str:
        countMap = {}
        groups = {}
        res = []
        for c in s:
            if c in countMap:
                countMap[c] += 1
            else:
                countMap[c] = 1

        for char, cnt in countMap.items():
            if cnt in groups:
                groups[cnt].append(char)
            else:
                groups[cnt] = [char]
        
        for i in range(len(s), 0, -1):
            if i in groups:
                for c in groups[i]:
                    res.append(c * i)

        return ''.join(res)