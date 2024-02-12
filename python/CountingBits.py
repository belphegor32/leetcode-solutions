from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
        
        return ans


    # n*log(n) solution
    #    res = []

    #    for i in range(n + 1):
    #        i = bin(i)[2:]
    #        res.append(i.count("1"))
        
    #    return res
