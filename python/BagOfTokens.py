from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # sort the input, so we know which tokens are better to play face up and which are better to play face down
        tokens.sort()
        res, cur_val = 0, 0
        l = 0
        r = len(tokens) - 1


        while l <= r:
            # we play the smallest tokens face up
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                cur_val += 1
                res = max(res, cur_val)
            # we play the biggest tokens face down
            elif cur_val > 0:
                power += tokens[r]
                r -= 1
                cur_val -= 1
            else:
                break
        
        return res