# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers_origin(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            n = 0
            if l1 and l2:
                n = l1.val + l2.val + carry
            elif l1 and not l2:
                n = l1.val + carry
            elif l2 and not l1:
                n = l2.val + carry
            else:
                n = carry
            cur.next = ListNode(n % 10)
            carry = n // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return dummy.next

    def addTwoNumbers_cleaner(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            n = val_1 + val_2 + carry
            cur.next = ListNode(n % 10)
            carry = n // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return dummy.next
