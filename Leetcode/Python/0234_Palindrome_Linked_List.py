# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(node):
            prev = None
            while node != None:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        if not head:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        reversedNode = reverse(slow)

        while reversedNode:
            if reversedNode.val != head.val:
                return False
            reversedNode = reversedNode.next
            head = head.next
        return True
