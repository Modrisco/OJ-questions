/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<Integer> preorder_stack(Node root) {
        List<Integer> nodes = new LinkedList<>();
        Stack<Node> stack = new Stack<>();
        if (root == null) {
            return nodes;
        }
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            nodes.add(node.val);
            List<Node> children = node.children;
            Collections.reverse(children);
            for (Node child: children) {
                stack.push(child);
            }
        }
        return nodes;
    }

    // recursive
    public List<Integer> preorder_recursive(Node root) {
        List<Integer> list = new LinkedList<>();
        helper(root, list);
        return list;
    }
    private void helper(Node root, List<Integer> list) {
        if (root == null) {
            return;
        }
        list.add(root.val);
        for (Node child: root.children) {
            helper(child, list);
        }
    }
}