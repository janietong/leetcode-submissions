# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        result = []
        count = 1
        while prev:
            if count != n:
                result.append(prev.val)
            prev = prev.next
            count += 1
        
        dummy = ListNode(0)
        newHead = dummy
        for val in reversed(result):
            newHead.next = ListNode(val)
            newHead = newHead.next
        
        return dummy.next
        