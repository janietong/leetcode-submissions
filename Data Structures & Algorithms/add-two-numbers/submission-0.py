# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h1 = l1
        h2 = l2
        dummy = ListNode(0)
        cur = dummy

        while h1 or h2 or carry:
            h1val = h1.val if h1 else 0
            h2val = h2.val if h2 else 0
            curVal = h1val + h2val + carry
            carry = curVal // 10
            val = curVal % 10

            cur.next = ListNode(val)
            cur = cur.next
            if h1:
                h1 = h1.next
            
            if h2:
                h2 = h2.next
        
        return dummy.next