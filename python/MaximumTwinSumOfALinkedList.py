from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        res = 0
        
        # we reverse a linked list all the way until the slow reaches the middle of a linked list
        while fast and fast.next:
            fast = fast.next
            fast = fast.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # slow pointer will go from middle all the way to the end, while prev will go to the beggining following the reverse links
        while slow and prev:
            res = max(res, slow.val + prev.val)
            prev = prev.next
            slow = slow.next
        
        return res