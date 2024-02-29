from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    pass
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        evenLevel = 1
        q = deque([root])

        # run bfs on a tree
        while q:
            if evenLevel == 1:
                prev = -10**20
            else:
                prev = 10**20
            for i in range(len(q)):
                node = q.popleft()

                # if the level is even, we want values to be odd and in increasing order
                if evenLevel == 1:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                # if the level is odd, we want values to be even and in decreasing order
                elif evenLevel == 0:
                    if node.val % 2 != 0 or node.val >= prev:
                        return False

                # append values to queue from left to right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                # update prev
                prev = node.val

            # update level is even or odd
            if evenLevel == 0:
                evenLevel = 1
            else:
                evenLevel = 0    
        
        return True