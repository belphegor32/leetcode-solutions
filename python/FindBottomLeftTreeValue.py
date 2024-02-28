from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    pass
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # we traverse tree level by level from right to left, so the last val in queue will be the answer
        q = deque([root])
        node = None
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
        
        return node.val