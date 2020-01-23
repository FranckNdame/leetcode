# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Solution 1: 156ms (93.82%) & 28MB (100)
    # Time Complexity: O(m + n) || Space Complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        pA, pB = headA, headB
        counter = 2
        
        while counter >= 0 and pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            if pA == headB or pB == headA: counter -= 1

        return pA if pA == pB else None

    
    # Solution 2: 176ms (22.66&) & 28MB (100%)
    # Time Complexity: O(m + n) || Space Complexity: O(m)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lookup = {}
        
        currA = headA
        currB = headB
        
        while currA:
            lookup[currA] = True
            currA = currA.next
            
        while currB:
            if currB in lookup:
                return currB
            currB = currB.next
        
        return None

# Solution 3: 164ms (73.83%) & 28MB (100%)
# Time Complexity: O(m + n) || Space Complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        
        currA = headA
        currB = headB
        
        while currA:
            lenA += 1
            currA = currA.next
            
        while currB:
            lenB += 1
            currB = currB.next
            
        offset = abs(lenA-lenB)
        currA = headA
        currB = headB
        while lenA > lenB and offset > 0:
            currA = currA.next
            offset -= 1
        
        while lenB > lenA and offset > 0:
            currB = currB.next
            offset -= 1
            
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
            
        return None

        

            
            
            
            
            
        