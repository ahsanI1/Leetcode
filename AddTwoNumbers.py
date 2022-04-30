# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while(l1 is not None and l2 is not None):
            sums = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode(sums % 10)
            carry = floor(sums / 10)
            cur = cur.next
            
        while(l1):
            sums = carry + l1.val
            carry = floor(sums/10)
            cur.next = ListNode(sums % 10)
            cur = cur.next
            l1 = l1.next
        while(l2):
            sums = carry + l2.val
            carry = floor(sums/10)
            cur.next = ListNode(sums % 10)
            cur = cur.next
            l2 = l2.next
            
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next
