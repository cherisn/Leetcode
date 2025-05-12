# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0  # Start with 0 as the decimal result

        # Traverse the linked list
        while head:
    # Left shift result by 1 (multiply by 2) and add current node's value (0 or 1)
            res = res * 2 + head.val
            head = head.next # Move to the next node

        # Return the final decimal value
        return res