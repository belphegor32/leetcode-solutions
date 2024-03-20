class ListNode:
    pass
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        right = list1
        n = 0
        # move right until the left boundary
        while n < a - 1:
            right = right.next
            n += 1
        # assign left to the left boundary
        left = right

        # move right to the right boundary
        while n <= b:
            right = right.next
            n += 1

        # assign left boundary next node the beggining of list2
        left.next = list2

        # go to the end of list2
        while list2.next:
            list2 = list2.next
        
        # assign the end of list2 to the right boundary
        list2.next = right

        return list1