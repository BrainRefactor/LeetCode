#
# https://leetcode.com/problems/add-two-numbers/
#
# Space Complexity: O(N)
# Time Complexity: O(N)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbersHelper(l1, l2)

    def addTwoNumbersHelper(self, l1, l2, carry=0):

        val = l1.val + l2.val + carry
        carry = val // 10
        remainder = val % 10

        node = ListNode(remainder)

        """
        If there are more digits or a carry to continue with, we just add few more nodes
        with the value as 0
        """

        if l1.next or l2.next or carry:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            node.next = self.addTwoNumbersHelper(l1.next, l2.next, carry=carry)
        return node

    def addTwoNumbersIterativeHelper(self, l1, l2):

        a = l1
        b = l2

        carry = 0
        head = None
        current = None

        while a or b:
            val = a.val + b.val + carry

            carry = val // 10
            remainder = val % 10

            if head is None:
                head = current = ListNode(remainder)
            else:
                current.next = ListNode(remainder)
                current = current.next

            """
            In cases where the no of digits don't match or else there is carry
            we'll just extend the nodes and set the value to 0
            pretty much the same as the above in case of recursive way
            """
            if a.next or b.next:
                if a.next is None:
                    a.next = ListNode(0)
                if b.next is None:
                    b.next = ListNode(0)
            if carry > 0:
                current.next = ListNode(carry)
            a = a.next
            b = b.next
        return head
