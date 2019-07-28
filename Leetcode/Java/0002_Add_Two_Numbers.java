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
        ListNode head = new ListNode(-1);
        ListNode curr = head;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int val_1 = (l1 != null) ? l1.val : 0;
            int val_2 = (l2 != null) ? l2.val : 0;
            int sum = val_1 + val_2 + carry;
            curr.next = new ListNode(sum % 10);
            carry = (sum >= 10) ? 1 : 0;
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
            curr = curr.next;
        }
        return head.next;
    }
}