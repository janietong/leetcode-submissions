# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while head:
            count = 0
            test = head

            while count < k and test:
                test = test.next
                count += 1
            
            if count < k:
                cur.next = head
                break

            prev = None
            curr = head
            newK = k
            while newK > 0:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                newK -= 1
            
            cur.next = prev
            head.next = curr

            cur = head
            head = curr
        return dummy.next
        