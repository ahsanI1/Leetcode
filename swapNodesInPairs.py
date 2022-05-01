# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        if head.next == None:
            return head
        
        dummy = ListNode(-1)
        ans = dummy
        curr = head
        ahead = head.next
        
        while(ahead != None):
            
            ans.next = ListNode(ahead.val)
            ans = ans.next
            
            ans.next = ListNode(curr.val)
            ans = ans.next
            
            if ahead.next != None:
                ahead = ahead.next.next
                curr = curr.next.next
            else:
                ahead = ahead.next
                
        if curr.next == None:
            ans.next = ListNode(curr.val)
        return dummy.next
