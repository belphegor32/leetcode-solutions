from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def backtracking(i):
            # if the index is out of bound, we add string to the res
            if i == len(s):
                res.append(cur[::])
                return
            
            for j in range(i, len(s)):
                # check if the string is a palindrome
                if self.isPalindrome(s, i, j):
                    cur.append(s[i:j+1])
                    # check for palindrome strings that start with the next index
                    backtracking(j + 1)
                    cur.pop()
        
        backtracking(0)
        return res
    
    # helper function to check palindromes
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True