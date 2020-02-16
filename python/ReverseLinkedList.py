# 
# 
# https://leetcode.com/problems/reverse-linked-list/
# 
# Time Complexity : O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursion(head)
    
    def recursion(self, head):
        if head is None or head.next is None:
            return head
        
        reverse = self.recursion(head.next)
        head.next.next = head
        head.next = None
        
        return reverse
    
    def iterative(self, head):
        current = head
        prev = None
        
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev

