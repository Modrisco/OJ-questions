/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode root = null;
        if (nums.length == 0) {
            return root;
        }
        int mid = nums.length / 2;
        root = new TreeNode(nums[mid]);
        int[] left = Arrays.copyOfRange(nums, 0, mid);
        int[] right = Arrays.copyOfRange(nums, mid + 1, nums.length);
        root.left = this.sortedArrayToBST(left);
        root.right = this.sortedArrayToBST(right);
        return root;
    }
}