# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode_Naive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = 0
        start = 0
        curr = head
        res = head
        while curr != None:
            size += 1
            curr = curr.next
        mid = size // 2
        while start < mid:
            res = res.next
            start += 1
        return res
    def middleNode_Two_Pointer(self, head):
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
