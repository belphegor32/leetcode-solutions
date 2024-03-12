from typing import Optional


# Definition for singly-linked list.
class ListNode:
    pass
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        prev_sums = set([0])
        summ = 0
        right = head
        while right:
            nums.append(right.val)
            summ += right.val
            # if the summ is in the prev_sums, that means that we have some part of the array that added up to zero so we need to remove it
            if summ in prev_sums:
                cur_sum = summ
                summ -= nums[-1]
                nums.pop()
                # we remove the part which added up to zero, we will now that, when the summ will be the same as cur_sum once again
                while summ != cur_sum:
                    prev_sums.remove(summ)
                    summ -= nums[-1]
                    nums.pop()
            else:
                prev_sums.add(summ)
            right = right.next
        
        dummy = ListNode()
        right = dummy
        # build new linked list
        for n in nums:
            right.next = ListNode(n)
            right = right.next

        return dummy.next  