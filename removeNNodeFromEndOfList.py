# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        while(fast.next != None):
            fast = fast.next
            if i >= n:
                slow = slow.next
            i+=1
        slow.next = slow.next.next
        return dummy.next
