/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    // https://www.cnblogs.com/grandyang/p/4128461.html
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA.next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB.next;
            }
        }
        while (headA != null && headB != null && headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        if (headA != null && headB != null) {
            return headA;
        } else {
            return null;
        }
    }

    final private int getLength(ListNode node) {
        int len = 0;
        while (node != null) {
            len++;
            node = node.next;
        }
        return len;
    }


    // Solution 2:
    // Loop
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode currA = headA;
        ListNode currB = headB;
        while (currA != currB) {
            currA = (currA == null) ? headB : currA.next;
            currB = (currB == null) ? headA : currB.next;
        }
        return (currA != null) ? currA : null;
    }
}