/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null | carry == 1) {
            int val_1 = (l1 != null) ? l1.val : 0;
            int val_2 = (l2 != null) ? l2.val : 0;
            int n = val_1 + val_2 + carry;
            cur.next = new ListNode(n % 10);
            carry = (int) Math.floor(n / 10);
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
            cur = cur.next;
        }
        return dummy.next;
    }
}
