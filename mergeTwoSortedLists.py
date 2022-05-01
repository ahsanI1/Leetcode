# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        walker = dummy
        while(l1 != None or l2 != None):
            if l1 == None:
                walker.next = ListNode(l2.val)
                walker = walker.next
                
                l2 = l2.next
            elif l2 == None:
                walker.next = ListNode(l1.val)
                walker = walker.next
                
                l1 = l1.next
            else: 
                a = l1.val
                b = l2.val

                if a < b:
                    walker.next = ListNode(a)
                    walker = walker.next

                    l1 = l1.next
                else:
                    walker.next = ListNode(b)
                    walker = walker.next

                    l2 = l2.next
            
        return dummy.next
