# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = self.getCount(head)
        isEven = self.getCount(head) % 2 == 0
        mid = length // 2 if isEven else (length // 2) + 1
        pointer = head
        runner = head
        counter = 0
        
        while counter < mid:
            runner = runner.next
            counter += 1
        
        runner = self.reverseList(runner)
        
        while runner:
            if pointer.val != runner.val:
                return False
            pointer = pointer.next
            runner = runner.next
            
        return True
    
    def getCount(self, root):
        count = 0
        curr = root
        
        while curr:
            count += 1
            curr = curr.next
        
        return count
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        next_ = curr.next
        
        while curr.next:
            curr.next = prev
            
            prev = curr
            curr = next_
            next_ = curr.next
        curr.next = prev
        
        return curr
        