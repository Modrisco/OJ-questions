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
    // Solution 1
    public boolean isUnivalTree(TreeNode root) {
        if (root == null) {
            return false;
        }
        int value = root.val;
        List<Integer> list = new LinkedList<>();
        helper(root, value, list);
        return list.size() == 0 ? true : false;
    }

    private void helper1(TreeNode root, int value, List<Integer> list) {
        if (root == null) {
            return;
        }
        if (root.val != value) {
            list.add(0);
        } else {
            helper(root.left, value, list);
            helper(root.right, value, list);
        }
    }
    // Solution 2
    public boolean isUnivalTree(TreeNode root) {
        if (root == null) {
            return false;
        }
        int value = root.val;
        return helper(root, value);
    }

    private boolean helper2(TreeNode root, int value) {
        if (root == null) {
            return true;
        } else if (root.val != value) {
            return false;
        } else {
            if (!helper(root.left, value)) {
                return false;
            }
            if (!helper(root.right, value)) {
                return false;
            }
        }
        return true;
    }
}