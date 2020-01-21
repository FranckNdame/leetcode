# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, 0)
    
    def helper(self, l1, l2, carry):
        if not l1 and not l2:
            if carry > 0: return ListNode(carry)
        if not l1: 
            if carry > 0: self.compute(l2, carry)
            return l2
        if not l2: 
            if carry > 0: self.compute(l1,carry)
            return l1
        
        value = l1.val + l2.val + carry
        l1.val = value % 10
        l1.next = self.helper(l1.next, l2.next, value//10)
        
        return l1
    
    def compute(self, ll, carry):
        value = ll.val + carry
        ll.val = value % 10
        ll.next = self.helper(ll.next, None, value//10)
        
        