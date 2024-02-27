class Solution:
    def numDecodings(self, s: str) -> int:
        # caching
        cache = { len(s) : 1 }
        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            # if char is one, then char after it can be any, but if its 2, it can only be 1 thru 6, since there are 26 letters in the alphabet
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456") )):
                res += dfs(i + 2)
            
            cache[i] = res
            return res

        return dfs(0)